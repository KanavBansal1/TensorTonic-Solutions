import numpy as np

def matrix_transpose(A: list) -> np.ndarray:

    rows = len(A)
    cols = len(A[0])

    result = []

    for j in range(cols):
        temp = []

        for i in range(rows):
            temp.append(A[i][j])

        result.append(temp)

    return np.asarray(result)
        
    # Write code here
    
