"""
MNIST数字分类

本脚本用于训练神经网络，对来自MNIST数据集的手写数字进行分类。它包括数据加载、模型定义、训练和评估过程。

用法：
1. 确保已安装所需的依赖项。
2. 运行此脚本以训练和评估模型。

注意：
- 训练完成的模型将保存为当前目录下的 'model.pth' 文件。

依赖项：
- PyTorch
- torchvision
- NumPy
"""

import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch import optim, nn
from model import NeuralNet  # 从 model.py 中导入 NeuralNet

# 设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载 MNIST 数据集
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_set = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_set = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
test_loader = DataLoader(test_set, batch_size=64, shuffle=False)

# 实例化 NeuralNet
model = NeuralNet().to(device)

# 定义损失函数和优化器
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# 训练模型的函数
def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)
        pred = model(X)
        loss = loss_fn(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


# 评估模型的函数
def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


# 主函数
if __name__ == "__main__":
    epochs = 5
    for t in range(epochs):
        print(f"Epoch {t + 1}\n-------------------------------")
        train(train_loader, model, loss_fn, optimizer)
        test(test_loader, model, loss_fn)
    print("Done!")
    torch.save(model.state_dict(), './model.pth')
