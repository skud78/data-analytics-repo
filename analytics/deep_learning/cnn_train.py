import torch
from torch.utils.data import DataLoader

def train_cnn(model, train_dataset, epochs=5, lr=0.001, batch_size=32):
    loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        total_loss = 0

        for images, labels in loader:
            optimizer.zero_grad()
            preds = model(images)
            loss = criterion(preds, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f"Epoch {epoch} Loss {total_loss:.4f}")

    return model
