import torch
from torchvision import datasets, transforms

from analytics.deep_learning.cnn_model import SimpleCNN
from analytics.deep_learning.cnn_train import train_cnn
from analytics.deep_learning.cnn_evaluate import evaluate_cnn

transform = transforms.Compose([
    transforms.ToTensor()
])

train_data = datasets.MNIST(root="datasets", train=True, download=True, transform=transform)
test_data = datasets.MNIST(root="datasets", train=False, download=True, transform=transform)

model = SimpleCNN(num_classes=10)

model = train_cnn(model, train_data, epochs=5)
metrics = evaluate_cnn(model, test_data)

print(metrics)
