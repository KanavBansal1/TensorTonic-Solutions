import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    ans = []

    for i in range(0,len(v)):
        temp = []

        for j in range(0,len(v)):

            if i != j:
                temp.append(0)
            else:
                temp.append(v[i])

        ans.append(temp)

    return np.array(ans)