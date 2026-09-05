from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = np.asarray(x, dtype=np.float32)

    mode = 0
    values, counts = np.unique_counts(x)
    x_tmp = counts == np.max(counts)
    
    for i in range(x_tmp.shape[0]):
        if x_tmp[i] == True:
            mode = values[i]
            break
    

    return {
        "mean": float(np.mean(x)),
        "median": float(np.median(x)),
        "mode": float(mode)
    }