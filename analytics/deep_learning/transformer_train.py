import torch
from torch.utils.data import DataLoader, TensorDataset

def train_transformer(model, X_train, y_train, epochs=5, lr=0.001, batch_size=32):
    X_train = torch.tensor(X_train, dtype=torch.long)
    y_train = torch.tensor(y_train, dtype=torch.long)

    dataset = TensorDataset(X_train, y_train)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        total_loss = 0

        for seq, labels in loader:
            optimizer.zero_grad()
            preds = model(seq)
            loss = criterion(preds, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f"Epoch {epoch} Loss {total_loss:.4f}")

    return model
