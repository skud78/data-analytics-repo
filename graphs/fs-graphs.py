import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Manual Completed', 'Manual Open', '3P Completed', '3P Open', 'CSS Completed', 'CSS Open']
time_buckets = ['<2 days', '2-4 days', '4-10 days', '>10 days']
raw_data = np.array([
  	[163, 14, 11, 0],  # Manual Completed
    [0, 0, 0, 0],  # Manual Open
    [16, 0, 0, 0],    # 3P Completed
    [0, 3, 0, 0],    # 3P Open
    [5, 0, 0, 0],    # CSS Completed
    [18, 4, 2, 0],   # CSS Open
])

# Normalize each row to sum to 100 (avoid division by zero)
normalized = np.array([
    (row / row.sum()) * 100 if row.sum() > 0 else row
    for row in raw_data
])

# Plot setup
x = np.arange(len(time_buckets))  # x-axis positions
width = 0.13

fig, ax = plt.subplots(figsize=(12, 6))

for i, row in enumerate(normalized):
    ax.bar(x + i * width, row, width, label=categories[i])

# Labels and formatting
ax.set_xlabel('Resolution Time')
ax.set_ylabel('% of Category')
ax.set_title('Normalized Issue Distribution by Resolution Time')
ax.set_xticks(x + width * (len(categories)-1) / 2)
ax.set_xticklabels(time_buckets)
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()