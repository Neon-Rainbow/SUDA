"""
该模块定义了一个简单的神经网络模型，用于基本的图像识别任务。
它包含一个神经网络类 `NeuralNet`，该类继承自 `torch.nn.Module`。

Module: model.py
"""

from torch import nn


# 定义神经网络模型
class NeuralNet(nn.Module):
    """
    这个类实现了一个简单的神经网络，用于图像识别任务。
    它包含两个主要部分：一个将输入图像展平的层和一个线性激活函数堆叠。

    Class: NeuralNet
    Extends: nn.Module
    """
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 10),
            nn.LogSoftmax(dim=1)
        )

    def forward(self, x):
        """
        定义模型的前向传播逻辑。

        Args:
            x (Tensor): 输入数据。

        Returns:
            Tensor: 模型的输出。

        Method: forward
        """
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
