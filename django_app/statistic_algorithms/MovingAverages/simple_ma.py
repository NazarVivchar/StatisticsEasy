import matplotlib.pyplot as plt
import numpy as np


def movingaverage(value, step):
    weights = np.repeat(1.0, step) / step
    result = np.convolve(value, weights, 'same')
    output = []
    for x in result:
        output.append(x)
    return output


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

    return out, movingaverage(outlist, 6), outlist

