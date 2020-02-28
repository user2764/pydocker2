import numpy as np

def first_f(a):
    if a%2 != 0:
        return str(a)+":a - must be even"
    return np.arange(0, a).reshape((2,int(a/2)))
