import numpy as np

# -----------------------------
# ARRAY CREATION
# -----------------------------
def create_array(data):
    """Create a NumPy array from a list or nested list."""
    return np.array(data)

def zeros(shape):
    """Create an array of zeros."""
    return np.zeros(shape)

def ones(shape):
    """Create an array of ones."""
    return np.ones(shape)

def arange(start, stop, step=1):
    """Create a range of values."""
    return np.arange(start, stop, step)

def linspace(start, stop, num=50):
    """Create evenly spaced values."""
    return np.linspace(start, stop, num)

# -----------------------------
# RESHAPING
# -----------------------------
def reshape(arr, new_shape):
    """Reshape an array."""
    return arr.reshape(new_shape)

def flatten(arr):
    """Flatten an array."""
    return arr.flatten()

# -----------------------------
# VECTORISED OPERATIONS
# -----------------------------
def add(arr1, arr2):
    return np.add(arr1, arr2)

def subtract(arr1, arr2):
    return np.subtract(arr1, arr2)

def multiply(arr1, arr2):
    return np.multiply(arr1, arr2)

def divide(arr1, arr2):
    return np.divide(arr1, arr2)

def elementwise_power(arr, power):
    return np.power(arr, power)

# -----------------------------
# MATRIX OPERATIONS
# -----------------------------
def dot(a, b):
    """Dot product."""
    return np.dot(a, b)

def matmul(a, b):
    """Matrix multiplication."""
    return np.matmul(a, b)

def transpose(a):
    """Transpose a matrix."""
    return np.transpose(a)

def inverse(a):
    """Matrix inverse."""
    return np.linalg.inv(a)

# -----------------------------
# STATISTICS
# -----------------------------
def mean(arr):
    return np.mean(arr)

def median(arr):
    return np.median(arr)

def std(arr):
    return np.std(arr)

def var(arr):
    return np.var(arr)

def min_val(arr):
    return np.min(arr)

def max_val(arr):
    return np.max(arr)

# -----------------------------
# RANDOM SAMPLING
# -----------------------------
def random_uniform(low=0.0, high=1.0, size=1):
    return np.random.uniform(low, high, size)

def random_normal(mean=0.0, std=1.0, size=1):
    return np.random.normal(mean, std, size)

def random_integers(low, high, size=1):
    return np.random.randint(low, high, size)
