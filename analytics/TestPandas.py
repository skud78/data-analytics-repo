import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
df = pd.DataFrame(data)

# Print the DataFrame
print("Original DataFrame:")
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print("\nAverage Age:", average_age)