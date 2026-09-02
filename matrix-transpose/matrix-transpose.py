import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    A = np.asarray(A)
    m, n = A.shape
    
    arr = np.zeros((n, m), dtype=A.dtype)

    for i in range(n):
        for j in range(m):
            arr[i, j] = A[j, i]
    
    return arr
