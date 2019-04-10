import matplotlib.pyplot as plt
import numpy as np

def weight_moving_average(data, step):
    buffer = [np.nan] * step
    for i in range(step, len(data)):
        buffer.append((data[i - step: i] * (np.arange(step) + 1)).sum() / (np.arange(step) + 1).sum())

    out = []
    for i in range(len(data)):
        out.append(i)
    return buffer,out
