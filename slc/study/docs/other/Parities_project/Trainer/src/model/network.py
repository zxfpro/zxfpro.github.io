import numpy as np
import torch
import torch.nn as nn

net1 = nn.Sequential(
    nn.Linear(2, 10),
    nn.LeakyReLU(0.3),
)
