import numpy as np
from analytics.deep_learning.lstm_model import SimpleLSTM
from analytics.deep_learning.lstm_train import train_lstm
from analytics.deep_learning.lstm_evaluate import evaluate_lstm

# Example synthetic time series
data = np.sin(np.linspace(0, 100, 500))

# Create sequences
def create_sequences(data, seq_len=10):
    X, y = [], []
    for i in range(len(data) - seq_len):
        X.append(data[i:i+seq_len])
        y.append(data[i+seq_len])
    return np.array(X), np.array(y)

seq_len = 10
X, y = create_sequences(data, seq_len)

# Reshape for LSTM: (samples, seq_len, features)
X = X.reshape(-1, seq_len, 1)

# Train/test split
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Build model
model = SimpleLSTM(input_dim=1, hidden_dim=64, num_layers=1, output_dim=1)

# Train
model = train_lstm(model, X_train, y_train, epochs=50)

# Evaluate
metrics = evaluate_lstm(model, X_test, y_test)
print(metrics)
