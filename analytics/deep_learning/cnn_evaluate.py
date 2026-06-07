import torch
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score

def evaluate_cnn(model, test_dataset):
    loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    all_preds = []
    all_labels = []

    for images, labels in loader:
        preds = model(images)
        preds = preds.argmax(dim=1)

        all_preds.extend(preds.numpy())
        all_labels.extend(labels.numpy())

    return {
        "accuracy": accuracy_score(all_labels, all_preds)
    }
