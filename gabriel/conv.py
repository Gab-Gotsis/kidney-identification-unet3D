import torch
import torch.nn as nn
import torch.nn.functional as F

#sample, numbers of channnels are currently not configured
class NetConv(nn.Module):
    def __init__(self):
        super(NetConv, self).__init__()
        self.flatten = nn.Flatten(1,3)
        self.conv1 = nn.Conv2d(1, 55, (15,15))
        self.conv2 = nn.Conv2d(55, 90, (12, 12))
        self.conv3 = nn.Conv2d(55, 90, (12, 12))
        self.in_to_out = nn.Linear(810,10)
        self.softmax = nn.LogSoftmax(dim=1)
        self.relu = nn.ReLU()
        self.maxpool = nn.MaxPool2d(2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = self.relu(x)
        x = self.conv3(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = self.in_to_out(x)
        x = self.softmax(x)
        return x 