#import numpy as np


def make_env(n=1000):
    #a = np.ones(n, dtype=np.int)
    a = range(n)
    return (a,), {}