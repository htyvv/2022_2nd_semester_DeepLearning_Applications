import torch
import torch.nn as nn
from ..utils import conv_bn


class ResidualBlock(nn.Module):
    def __init__(self, in_channels, res_channels, stride=1):
        super().__init__()
        self.shortcut = self.get_shortcut(in_channels, res_channels, stride)
        
        self.residual = nn.Sequential(
            conv_bn(in_channels, res_channels, stride=stride),
            nn.ReLU(inplace=True),
            conv_bn(res_channels, res_channels)
        )
        self.act = nn.ReLU(inplace=True)
        
        self.gamma = nn.Parameter(torch.zeros(1))
    
    def forward(self, x):
        out = self.shortcut(x) + self.gamma * self.residual(x)
        return self.act(out)
    
    def get_shortcut(self, in_channels, res_channels, stride):
        layers = []
        if stride > 1: layers.append(nn.AvgPool2d(stride))
        if in_channels != res_channels: layers.append(conv_bn(in_channels, res_channels, 1))
        return nn.Sequential(*layers)