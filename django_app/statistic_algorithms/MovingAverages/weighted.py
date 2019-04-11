import matplotlib.pyplot as plt
import numpy as np

def weight_moving_average(data, step):
    buffer = [np.nan] * step
    for i in range(step, len(data)):
        buffer.append((data[i - step: i] * (np.arange(step) + 1)).sum() / (np.arange(step) + 1).sum())

    out = []
    for i in range(len(data)):
        out.append(i)
    return buffer


def main(filename='media/input.txt'):
    with open(filename) as my_file:
        outlist = []
        for words in my_file:
            temp = words.split('\n')

            temp[0] = temp[0].replace('.', '')

            outlist.append(temp[0])


    outlist = [int(i) for i in outlist if int(i)>100000]

    out = []
    for i in range(len(outlist)):
        out.append(i)

    return out, weight_moving_average(outlist, 6), outlist
