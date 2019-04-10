import matplotlib.pyplot as plt
import numpy as np

def exponential(value, step):
    weights = np.exp(np.linspace(-1., 0., step))
    weights /= weights.sum()
    a = np.convolve(value, weights)[:len(value)]
    a[:step] = a[step]
    out = []
    for i in range(len(value)):
        out.append(i)
    return a,out