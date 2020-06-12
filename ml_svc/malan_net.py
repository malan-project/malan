import torch
import torch.nn as nn

class MalanNet(nn.Module):
    def __init__(self):
        super(MalanNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, 5, padding=0)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2, 2)
        self.dense1 = nn.Linear(64 * 6 * 6, 120)
        self.relu3 = nn.ReLU()
        self.dense2 = nn.Linear(120, 84)
        self.relu4 = nn.ReLU()
        self.dense3 = nn.Linear(84, 1)
        self.sigmoid1 = nn.Sigmoid()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.conv2(x) 
        x = self.relu2(x)
        x = self.pool2(x)
        x = x.view(-1, 64 * 6 * 6)
        x = self.dense1(x)
        x = self.relu3(x)
        x = self.dense2(x)
        x = self.relu4(x)
        x = self.dense3(x)
        x = self.sigmoid1(x)
        return x
