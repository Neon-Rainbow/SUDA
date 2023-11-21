from PIL import Image

from main import *

# 加载模型 (确保模型已经加载并在正确的设备上)
model = NeuralNet().to(device)
model.load_state_dict(torch.load('model.pth'))  # 加载训练好的模型参数
model.eval()


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


# 预测图像
image_path = 'path_to_your_image.jpg'  # 替换为您的图像路径
prediction = predict(image_path, model)
print(f'Predicted digit: {prediction}')
