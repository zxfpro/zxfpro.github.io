import os

import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as py
import matplotlib.pyplot as plt

import torch
from pytorch_lightning import (
    Trainer,
)
from pytorch_lightning.loggers import CSVLogger
from pytorch_lightning.callbacks.progress import TQDMProgressBar

from Parities_project.Trainer.src.dataset.sig_dataset import SigDataModule
from tqdm import tqdm
from Parities_project.Trainer.src.utils import tosig

test = SigDataModule(batch_size=32,level=4)
test.prepare_data()
a = test.show_batch(idx=1)
print(a)


## 1 252,16  1600epoch
## 10 2520 160  100epoch

AVAIL_GPUS = min(1, torch.cuda.device_count())
BATCH_SIZE = 1024 if AVAIL_GPUS else 32
WINDOW_SIZE = 8
LOGGER_PATH = ["log/CVAE/", "CVAE"]
MAX_EPOCHS = 100
level = 4
from Parities_project.Trainer.model.CVAE import CVAE

net = CVAE(WINDOW_SIZE, nhid=30, ncond=8, lr=0.001)
dm = SigDataModule(batch_size=BATCH_SIZE,level=level)
logger = CSVLogger(save_dir=LOGGER_PATH[0], name=LOGGER_PATH[1])
tqdmp = TQDMProgressBar()

trainer = Trainer(
    gpus=AVAIL_GPUS,
    max_epochs=MAX_EPOCHS,
    callbacks = tqdmp,
    logger=logger,
)
trainer.fit(net,dm)
print(2)











def plt_loss_picture(trainer,loss_name_list):
    loss_data = pd.read_csv(os.path.join(trainer.logger.log_dir, "metrics.csv"))
    #准备数据
    data_list = [go.Scatter(y=loss_data[loss],name=loss) for loss in loss_name_list]
    #准备显示
    layout = go.Layout(title='loss picture')
    fig = go.Figure(data=data_list,layout = layout)
    py.iplot(fig)

plt_loss_picture(trainer,["train_loss"])

loss_data = pd.read_csv(os.path.join(trainer.logger.log_dir, "metrics.csv"))
plt.semilogy(loss_data['train_loss'],)





#########
np.array([])

generated = np.array([net.generate(cond) for cond in dm.conditions])
#generated = MG.generate(MG.conditions[100], n_samples=len(MG.logsigs))
#generated = MG.generate(MG.conditions[150][2] * 0.5, n_samples=len(MG.logsigs))





generated_sigs = np.array([tosig.logsig2sig(logsig, 2, level) for logsig in tqdm(generated)])
real_sigs = np.array([tosig.logsig2sig(logsig, 2, level) for logsig in tqdm(dm.orig_logsig)])

from esig.tosig import sigkeys

keys = sigkeys(2, order).split()

PROJECTIONS = [(4, 5), (2, 4), (6, 7), (9, 2)]

plt.figure(figsize=(12, 8))
for i, projection in enumerate(PROJECTIONS):
    plt.subplot(2, 2, i + 1)

    plt.scatter(real_sigs[:, projection[0]], real_sigs[:, projection[1]],
                label="Real local")
    plt.scatter(generated_sigs[:, projection[0]], generated_sigs[:, projection[1]],
                label="Generated")
    plt.xlabel(keys[projection[0]], fontsize=14)
    plt.ylabel(keys[projection[1]], fontsize=14)
    plt.xticks([])
    plt.yticks([])
    # plt.legend()

plt.show()

import process_discriminator

normalised_generated = np.array([MG.generate(cond, normalised=True) for cond in MG.conditions])
sigs1 = np.array([tosig.logsig2sig(logsig, 2, order) for logsig in tqdm(normalised_generated)])
sigs2 = np.array([tosig.logsig2sig(logsig, 2, order) for logsig in tqdm(MG.logsigs)])

res = process_discriminator.test(sigs1, sigs2, order=order, compute_sigs=False,
                                 confidence_level=0.99)

print("Are the generated and real distributions DIFFERENT? {}".format(res))


import logsig_inversion
from esig.tosig import stream2logsig
from Parities_project.Trainer.src.utils import leadlag

logsig = MG.generate(MG.conditions[0])

%%time
pip = 0.0001 #0.01
n_pips = 5 * 10000
n_points = 21#21

n_iterations = 100 #循环次数
n_organisms = 400 #生物

recovered_path, loss = logsig_inversion.train(logsig, order, n_iterations, n_organisms, n_points,
                                              pip, n_pips)


plt.plot(recovered_path)
plt.show()
print(f"Target log-signature: {logsig.tolist()}")
print(f"Recovered log-signature: {stream2logsig(leadlag(recovered_path), order).tolist()}")

paths = []
for condition in tqdm(MG.conditions):
    logsig = MG.generate(condition)
    recovered_path, loss = logsig_inversion.train(logsig, order, n_iterations, n_organisms, n_points,
                                                  pip, n_pips)

    paths.append(recovered_path)

import matplotlib.patches as mpatches

plt.figure(figsize=(8, 6))
for path1, path2 in zip(paths, MG.windows):
    returns = path2[::2, 1][:20] - path2[0, 1]
    plt.plot(returns, "C1", alpha=0.25)

    plt.plot(path1[:20], "C0", alpha=0.25)

blue_patch = mpatches.Patch(color='C0', label='Generated paths')
red_patch = mpatches.Patch(color='C1', label='Real paths')
plt.legend(handles=[blue_patch, red_patch], fontsize=12)
plt.xlabel("Days", fontsize=14)
plt.show()



generate_data = net.generate(class_idx=1,batch_size=1000)

log_return_data = generate_data.cpu().detach().numpy().astype('float')

def ran(x_one):
    def random_get(x):
        return np.random.uniform(low=dm.retbins[x], high=dm.retbins[x+1], size=None)
    for i in range(len(x_one)):
        x_one[i] = random_get(int(x_one[i]))

_ =[ran(i) for i in log_return_data]

price = 1.1076

price_data = price(log_return_data,axis=1)*price#

price_data[:,0]=price

plt.plot(price_data.T)
plt.show()

trainer.save_checkpoint('SOFR_30day.ckpt')

dm.retbins

# test_pycharm->notebook update
# test remote tokens
