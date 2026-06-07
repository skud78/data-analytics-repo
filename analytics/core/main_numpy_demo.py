from analytics.core.numpy_utils import (
    create_array, reshape, add, multiply,
    dot, matmul, mean, std, random_normal
)

# Create arrays
a = create_array([1, 2, 3])
b = create_array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)

# Vectorised math
print("a + b:", add(a, b))
print("a * b:", multiply(a, b))

# Matrix operations
A = reshape(create_array([[1, 2], [3, 4]]), (2, 2))
B = reshape(create_array([[5, 6], [7, 8]]), (2, 2))

print("Dot product:", dot(a, b))
print("Matrix multiply:\n", matmul(A, B))

# Statistics
print("Mean of a:", mean(a))
print("Std of a:", std(a))

# Random sampling
print("Random normal sample:", random_normal(mean=0, std=1, size=5))
