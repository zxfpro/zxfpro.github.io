#中等规模
import numpy as np
from collections import OrderedDict
import torch
import torch.nn as nn
from torch.nn import functional as F


from pytorch_lightning import (
    LightningDataModule,
    LightningModule,
    Trainer,
    seed_everything,
)


class MLP(nn.Module):
    def __init__(self, hidden_size, last_activation=True):
        """
        生成标准的全连接网络
        hidden_size,全连接隐藏层的层数,list
        last_activation,是否在全连接层最后加入BN层和ReLU层,BOOL
        """
        super().__init__()
        q = []
        for i in range(len(hidden_size) - 1):
            in_dim = hidden_size[i]
            out_dim = hidden_size[i + 1]
            q.append(("Linear_%d" % i, nn.Linear(in_dim, out_dim)))
            if (i < len(hidden_size) - 2) or (
                    (i == len(hidden_size) - 2) and (last_activation)
            ):
                q.append(("BatchNorm_%d" % i, nn.BatchNorm1d(out_dim)))
                q.append(("ReLU_%d" % i, nn.ReLU(inplace=True)))
        self.mlp = nn.Sequential(OrderedDict(q))

    def forward(self, x):
        return self.mlp(x)


class Flatten(nn.Module):
    def __init__(self):
        super(Flatten, self).__init__()

    def forward(self, x):
        batch_size = x.shape[0]
        return x.view(batch_size, -1)


class Encoder(nn.Module):
    def __init__(self, shape, nhid=16, ncond=1):
        super(Encoder, self).__init__()
        size = ((shape - 8) // 2 - 4) // 2
        self.encode = nn.Sequential(
            nn.Conv1d(1, 16, 5),
            nn.BatchNorm1d(16),
            nn.ReLU(inplace=True),
            nn.Conv1d(16, 32, 5),
            nn.BatchNorm1d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool1d(2),
            nn.Conv1d(32, 64, 3),
            nn.BatchNorm1d(64),
            nn.ReLU(inplace=True),
            nn.Conv1d(64, 64, 3),
            nn.BatchNorm1d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool1d(2),
            Flatten(),
            MLP([size * 64, 256, 128]),
        )
        self.calc_mean = MLP([128 + ncond, 64, nhid], last_activation=False)
        self.calc_logvar = MLP([128 + ncond, 64, nhid], last_activation=False)

    def forward(self, x, y=None):
        x = self.encode(x)
        y = Flatten()(y)
        if y is None:
            return self.calc_mean(x), self.calc_logvar(x)
        else:
            return self.calc_mean(torch.cat((x, y), dim=1)), self.calc_logvar(
                torch.cat((x, y), dim=1)
            )


###

class Decoder(nn.Module):
    def __init__(self, shape=252, nhid=16, ncond=1, num_vals=64):
        super(Decoder, self).__init__()
        self.decode = nn.Sequential(
            MLP([nhid + ncond, 64, 128, 128, shape], last_activation=False),
            nn.Sigmoid(),
            nn.Linear(shape, num_vals * shape)
        )
        self.num_vals = num_vals

    def forward(self, z, y=None):
        y = Flatten()(y)
        if y is None:
            h_d = self.decode(z)
        else:
            h_d = self.decode(torch.cat((z, y), dim=1))

        b = h_d.shape[0]  # 1024
        d = h_d.shape[1] // self.num_vals
        h_d = h_d.view(b, d, self.num_vals)
        mu_d = torch.softmax(h_d, 2)
        return mu_d

    def sample(self, z, y_hat):
        mu_d = self(z, y_hat)
        b = mu_d.shape[0]
        m = mu_d.shape[1]
        mu_d = mu_d.view(mu_d.shape[0], -1, self.num_vals)
        p = mu_d.view(-1, self.num_vals)
        x_new = torch.multinomial(p, num_samples=1).view(b, m)
        return x_new


PI = torch.from_numpy(np.asarray(np.pi))
EPS = 1.e-5


def log_categorical(x, p, num_classes=256, reduction=None, dim=None):
    x_one_hot = F.one_hot(x.long(), num_classes=num_classes)
    log_p = x_one_hot * torch.log(torch.clamp(p, EPS, 1. - EPS))
    if reduction == 'avg':
        return torch.mean(log_p, dim)
    elif reduction == 'sum':
        return torch.sum(log_p, dim)
    else:
        return log_p




def log_normal_diag(x, mu, log_var, reduction=None, dim=None):
    log_p = -0.5 * torch.log(2. * PI) - 0.5 * log_var - 0.5 * torch.exp(-log_var) * (x - mu) ** 2.
    if reduction == 'avg':
        return torch.mean(log_p, dim)
    elif reduction == 'sum':
        return torch.sum(log_p, dim)
    else:
        return log_p


class MoGPrior(nn.Module):
    def __init__(self, L, num_components):
        super(MoGPrior, self).__init__()

        self.L = L
        self.num_components = num_components

        # params
        self.means = nn.Parameter(torch.randn(num_components, self.L))
        self.logvars = nn.Parameter(torch.randn(num_components, self.L))

        # mixing weights
        self.w = nn.Parameter(torch.zeros(num_components, 1, 1))

    def get_params(self):
        return self.means, self.logvars

    def sample(self, batch_size):
        # mu, lof_var
        means, logvars = self.get_params()

        # mixing probabilities
        w = F.softmax(self.w, dim=0)
        w = w.squeeze()

        # pick components
        indexes = torch.multinomial(w, batch_size, replacement=True)

        # means and logvars
        eps = torch.randn(batch_size, self.L)
        for i in range(batch_size):
            indx = indexes[i]
            if i == 0:
                z = means[[indx]] + eps[[i]] * torch.exp(logvars[[indx]])
            else:
                z = torch.cat((z, means[[indx]] + eps[[i]] * torch.exp(logvars[[indx]])), 0)
        return z

    def log_prob(self, z):
        # mu, lof_var
        means, logvars = self.get_params()

        # mixing probabilities
        w = F.softmax(self.w, dim=0)

        # log-mixture-of-Gaussians
        z = z.unsqueeze(0) # 1 x B x L
        means = means.unsqueeze(1) # K x 1 x L
        logvars = logvars.unsqueeze(1) # K x 1 x L

        log_p = log_normal_diag(z, means, logvars) + torch.log(w) # K x B x L
        log_prob = torch.logsumexp(log_p, dim=0, keepdim=False) # B x L

        return log_prob



# 离散的
class CVAE(LightningModule):
    def __init__(self, shape=252, nhid=16, ncond=1, num_vals=64, lr=0.01):
        super().__init__()
        self.encoder = Encoder(shape, nhid, ncond=ncond)
        self.decoder = Decoder(shape=shape, nhid=nhid, ncond=ncond, num_vals=num_vals)
        self.dim = nhid
        self.lr = lr
        self.train_loss_list = []
        self.valid_loss_list = []
        self.smooth = nn.SmoothL1Loss()
        self.BCE_loss = nn.BCELoss(reduction="sum")
        self.prior = MoGPrior(L=nhid, num_components=8)
        self.num_vals = num_vals

    def training_step(self, batch, batch_idx):
        (X, y) = batch
        X_hat, mean, logvar, z = self(X, y)
        loss = self.loss(X, X_hat, mean, logvar, z)
        self.log("train_loss", loss, prog_bar=False)
        # self.log("train_acc", self.accuracy(y_hat, y), prog_bar=False)
        self.train_loss_list.append(loss)
        return loss


    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.lr)
        return optimizer

    def forward(self, x, y):
        x = x.reshape(x.shape[0], 1, x.shape[1])  ##todo
        mean, logvar = self.encoder(x, y)
        z = self.sampling(mean, logvar)

        return self.decoder(z, y), mean, logvar, z

    def loss(self, X, X_hat, mean, logvar, z):  #
        alpha = 1.0

        RE = log_categorical(X, X_hat, num_classes=self.num_vals, reduction='sum', dim=-1).sum(-1)

        KL_divergence = (self.prior.log_prob(z) - self.log_normal_diag(z, mean, logvar)).sum(-1)

        return -(RE + KL_divergence).mean()

    def log_normal_diag(self, x, mu, log_var, reduction=None, dim=None):
        # 标准正态
        log_p = -0.5 * torch.log(2. * PI) - 0.5 * log_var - 0.5 * torch.exp(-log_var) * (x - mu) ** 2.
        return log_p

    def sampling(self, mean, logvar):
        eps = torch.randn(mean.shape).to(self.device)
        sigma = torch.exp(0.5 * logvar)
        return mean + eps * sigma

    def generate(self, class_idx, batch_size=32):
        if type(class_idx) is int:
            class_idx = torch.tensor(class_idx)

        class_idx = class_idx.repeat(batch_size, 1)
        z = self.prior.sample(batch_size=batch_size)
        res = self.decoder.sample(z, class_idx)
        return res
