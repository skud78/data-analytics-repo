import torch
from torch.utils.data import DataLoader, TensorDataset

def train_lstm(model, X_train, y_train, epochs=50, lr=0.001, batch_size=32):
    X_train = torch.tensor(X_train, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)

    dataset = TensorDataset(X_train, y_train)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        total_loss = 0

        for seq, target in loader:
            optimizer.zero_grad()
            preds = model(seq)
            loss = criterion(preds, target)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        if epoch % 10 == 0:
            print(f"Epoch {epoch} Loss {total_loss:.4f}")

    return model
