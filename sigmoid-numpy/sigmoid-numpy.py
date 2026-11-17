import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:

    return 1 / (1 + np.exp(-np.array(x) if isinstance(x,list) else x))
    # Write code here
    pass