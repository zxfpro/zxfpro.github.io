from collections import OrderedDict
import torch
import torch.nn as nn
import logging
from pytorch_lightning import LightningModule

logging.basicConfig(level=logging.INFO)

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
    def __init__(self, common_network, mean_network, logvar_network):
        super().__init__()
        self.common_network = common_network
        self.mean_network = mean_network
        self.logvar_network = logvar_network

    def forward(self, x, cond=None):
        x_cond = torch.cat((x, cond), dim=1)
        x_cond = self.common_network(x_cond)
        mean, logvar = self.mean_network(x_cond), self.logvar_network(x_cond)
        return mean, logvar

class Decoder(nn.Module):
    def __init__(self, decode_network):
        super(Decoder, self).__init__()
        self.decode_network = decode_network

    def forward(self, x, cond=None):
        x_cond = torch.cat((x,cond),dim=1)
        x_cond = self.decode_network(x_cond)
        return x_cond

class CVAE(LightningModule):
    def __init__(self,common_network, mean_network, logvar_network,decode_network, optim,lr=0.001):
        super(CVAE, self).__init__()
        logging.info('struct init')
        
        self.encoder = Encoder(common_network, mean_network, logvar_network)
        logging.info('encoder_init_over')
        self.decoder = Decoder(decode_network)
        logging.info('decoder_init_over')
        self.optim = optim
        logging.info('optim_init_over')
        logging.info('struct init_over')
        self.lr = lr

    def _sample(self,mean,logvar):
        eps = torch.randn(mean.shape,device=self.device)
        sigma = torch.exp(0.5 * logvar)
        return mean + eps * sigma

    def forward(self, x,y):
        mean,logvar = self.encoder(x,y)
        z = self._sample(mean,logvar)
        x_hat = self.decoder(z,y)
        return x_hat,mean,logvar

    def loss2(self, X, X_hat, mean, logvar):  # X,self.dec,mn,sd
        alpha = 0.003
        smooth = nn.SmoothL1Loss()(X_hat, X)
        KL_divergence = torch.mean(torch.sum(-1 - logvar + torch.exp(logvar) + mean ** 2, dim=1), dim=0)

        # smooth =  (x-y)**2     
        return alpha * KL_divergence + smooth

    
    def loss3(self, X, X_hat, mean, logvar):  # X,self.dec,mn,sd
        alpha = 0.003
        KL_divergence = torch.mean(torch.sum(-1 - logvar + torch.exp(logvar) + mean ** 2, dim=1), dim=0)
        smooth = nn.MSELoss()(X,X_hat)
        return alpha * KL_divergence + smooth
        
        
    def loss(self, X, X_hat, mean, logvar):  # X,self.dec,mn,sd
        alpha = 0.003
        KL_divergence = 0.5*torch.sum(-1 - logvar + torch.exp(logvar) + torch.square(mean), dim=1)

        end = X - X_hat
        squ_dif =  torch.square(end)
        smooth = torch.sum(squ_dif)
        
        return torch.mean((1-alpha)*smooth +alpha *KL_divergence)
    
    def training_step(self, batch, batch_idx):
        (X, y) = batch
        X_hat,mean,logvar = self(X,y)
        loss = self.loss(X_hat,X,mean,logvar)
        # self.log('train_loss', loss)
        return loss

    def configure_optimizers(self):
        return self.optim(self.parameters(), lr=self.lr)

    def generate(self, cond, n_samples=None):
        self.eval()
        z_dim = 8
        if n_samples is not None:
            z = torch.randn((n_samples, z_dim))
            cond = torch.Tensor([list(cond)] * n_samples)
        else:
            z = torch.randn((1, z_dim))
            cond = torch.tensor(cond).reshape(1,-1).to(torch.float32)
        res = self.decoder(z, cond)
        # res = res.reshape(-1)
        return res



















