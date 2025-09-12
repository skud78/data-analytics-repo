import sys
sys.path.append('./lib')


import matplotlib.pyplot as plt
import numpy as np

# Categories and time intervals
categories = ['Manual Completed', 'Manual Open', '3P Completed', '3P Open', 'CSS Completed', 'CSS Open']
time_buckets = ['<2 days', '2-4 days', '4-10 days', '>10 days']
data = np.array([
	[163, 14, 11, 0],  # Manual Completed
    [0, 0, 0, 0],  # Manual Open
    [16, 0, 0, 0],    # 3P Completed
    [0, 3, 0, 0],    # 3P Open
    [5, 0, 0, 0],    # CSS Completed
    [18, 4, 2, 0],   # CSS Open
])

# Plot setup
x = np.arange(len(time_buckets))  # the label locations
width = 0.13  # width of the bars

fig, ax = plt.subplots(figsize=(12, 6))

# Create a bar for each category
for i in range(len(categories)):
    ax.bar(x + i * width, data[i], width, label=categories[i])

# Labeling
ax.set_xlabel('Resolution Time')
ax.set_ylabel('Count')
ax.set_title('Issue Completion/Open Status by Resolution Time')
ax.set_xticks(x + width * (len(categories)-1) / 2)
ax.set_xticklabels(time_buckets)
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()