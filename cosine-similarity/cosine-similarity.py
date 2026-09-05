import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if not norm_a or not norm_b:
        return float(0)

    return float(np.dot(a, b) / (norm_a * norm_b))