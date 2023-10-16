import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE

    n = data.shape[0]
    r = np.random.uniform(low=-10, high=10, size=n)
    for i in range(num_steps):
        r = (data @ r) / np.linalg.norm(data @ r, ord=2)
        mu = r.T @ (data @ r) / (r.T @ r)
    return float(mu), r