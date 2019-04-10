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
    return result



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

    return out, running_mean(outlist, 6), outlist
