import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert: list to 3x3 numpy array
    matrix = np.array(list)
    matrix = matrix.reshape(3,3)
    
    # Calculating
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()]
    max_val = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()]
    min_val = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
    sum_val = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }

    return calculations