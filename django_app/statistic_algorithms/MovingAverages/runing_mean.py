import matplotlib.pyplot as plt
import numpy as np

def running_mean(data, step):
    sum = 0
    result = list(0 for x in data)

    for i in range(0, step):
        sum = sum + data[i]
        result[i] = sum / (i + 1)

    for i in range(step, len(data)):
        sum = sum - data[i - step] + data[i]
        result[i] = sum / step

    out = []
    for i in range(len(data)):
        out.append(i)
    return result,out
