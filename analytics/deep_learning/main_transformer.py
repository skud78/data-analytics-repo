import numpy as np

from analytics.deep_learning.transformer_model import SimpleTransformer
from analytics.deep_learning.transformer_train import train_transformer
from analytics.deep_learning.transformer_evaluate import evaluate_transformer

# Toy vocabulary
word_to_id = {
    "good": 1, "great": 2, "excellent": 3,
    "bad": 4, "terrible": 5, "awful": 6
}

# Toy dataset
texts = [
    ["good", "great", "excellent"],
    ["bad", "terrible", "awful"],
    ["great", "good"],
    ["awful", "bad"]
]

labels = [1, 0, 1, 0]  # 1 = positive, 0 = negative

# Convert to IDs
max_len = 5
X = []

for t in texts:
    ids = [word_to_id[w] for w in t]
    ids += [0] * (max_len - len(ids))  # pad
    X.append(ids)

X = np.array(X)
y = np.array(labels)

# Build model
vocab_size = len(word_to_id) + 1
model = SimpleTransformer(vocab_size=vocab_size, num_classes=2)

# Train
model = train_transformer(model, X, y, epochs=10)

# Evaluate
metrics = evaluate_transformer(model, X, y)
print(metrics)
