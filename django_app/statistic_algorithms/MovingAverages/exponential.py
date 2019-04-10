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

    return a



def main(filename='media/input.txt'):
    with open(filename) as my_file:
        outlist = []
        for words in my_file:
            temp = words.split('\n')

            temp[0] = temp[0].replace('.', '')

            outlist.append(temp[0])


    outlist = [int(i) for i in outlist if int(i)>100000]
    print(outlist)
    out = []
    for i in range(len(outlist)):
        out.append(i)

    return out, exponential(outlist, 6), outlist