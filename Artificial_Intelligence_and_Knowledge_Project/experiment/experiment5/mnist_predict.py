"""
手写数字识别

这个脚本用于使用训练好的神经网络模型对手写数字图像进行识别。它包括图像预处理、模型加载和预测过程。

用法：
1. 确保已安装所需的依赖项并且已训练好模型（模型保存为 'model.pth'）。
2. 将要识别的手写数字图像放入 './predict_images/' 文件夹中。
3. 更新 'image_path' 变量以指定要识别的图像文件路径。
4. 运行脚本以获取识别结果。

依赖项：
- PyTorch
- NumPy
- Pillow
"""


import torch
from PIL import Image
import torchvision.transforms as transforms
from model import NeuralNet


# 图像预处理函数
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Grayscale(),  # 转换为灰度图
        transforms.Resize((28, 28)),  # 调整大小
        transforms.ToTensor(),  # 转换为Tensor
        transforms.Normalize((0.5,), (0.5,))  # 标准化
    ])

    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)  # 添加批量维度
    return image


# 预处理图像并预测
def predict(image_path, model):
    image = preprocess_image(image_path)
    image = image.to(device)

    with torch.no_grad():
        output = model(image)
        predicted = torch.argmax(output, dim=1)
    return predicted.item()


# 主执行块
if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 加载模型
    model = NeuralNet().to(device)
    model.load_state_dict(torch.load('model.pth'))  # 确保 model.pth 路径正确
    model.eval()

    # 预测图像
    image_path = './predict_images/5_handwrite_01.jpg'  # 替换为您的图像路径
    prediction = predict(image_path, model)
    print(f'Predicted digit: {prediction}')