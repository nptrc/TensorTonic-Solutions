import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    A = np.array(A)
    trace = 0

    for i in range(A.shape[0]):
        trace += A[i, i]

    return trace