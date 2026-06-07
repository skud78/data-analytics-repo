import torch
import torch.nn as nn

class SimpleTransformer(nn.Module):
    def __init__(self, vocab_size, embed_dim=64, num_heads=4, hidden_dim=128, num_layers=2, num_classes=2):
        super(SimpleTransformer, self).__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=num_heads,
            dim_feedforward=hidden_dim,
            batch_first=True
        )

        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

        self.fc = nn.Linear(embed_dim, num_classes)

    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        x = x.mean(dim=1)  # global average pooling
        return self.fc(x)
