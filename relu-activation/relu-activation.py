import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    arr = np.asarray(x, dtype=np.float32)
    return np.asarray(np.maximum(0.0, x))