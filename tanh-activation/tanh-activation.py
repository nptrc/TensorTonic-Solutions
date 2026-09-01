import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    arr = np.asarray(x, dtype=np.float32)
    return np.tanh(arr)