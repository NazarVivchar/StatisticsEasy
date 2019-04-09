from  matplotlib import mlab
from statistics import *
import math
import pandas as pd
import numpy as np
import scipy.stats as st
import pylab
import matplotlib.pyplot as plt
import random


def test(n = 100, p = 0.7):
    '''
    bernoulli distribution

    n - розмір вибірки
    p - ймовірність одиниці

    Повертає список вигляду [згенерована вибірка, список x, список y, середнє, мода, медіана,
    розмах, девіація, варіанса, стандарт, варіація, асиметрія, ексцес]
    '''

    distribution = st.bernoulli(p)
    sample = list(distribution.rvs(size = n))

    for i in range(len(sample)):
        sample[i] = round(sample[i], 2)
     
    var = list(sample)
    var.sort()
    x = list(set(sample))
    y = list()
    x.sort()

    freq_table = dict()

    for num in x:
        freq_table[num] = sample.count(num)

    int_len = ((max(sample) - min(sample)) / r(sample))
    int_bounds = list()
    next = min(sample)

    for i in range(r(sample)):
        int_bounds.append(round(next, 2))
        next += int_len

    int_bounds.append(max(sample))

    freq_table = dict()
    int_list = list()

    for i in range(len(int_bounds)-1):
        int_list.append([int_bounds[i], int_bounds[i+1]])

    for i in range(len(int_list)):
        if i != len(int_list)-1:
            freq_table["[" + str(int_list[i][0]) + "; " + str(int_list[i][1]) + ")"] = 0
        else:
            freq_table["[" + str(int_list[i][0]) + "; " + str(int_list[i][1]) + "]"] = 0

    for i in range(len(sample)):
        for j in range(len(int_list)):
            if sample[i] >= int_list[j][0] and sample[i] < int_list[j][1] and j != len(int_list)-1:
                freq_table["[" + str(int_list[j][0]) + "; " + str(int_list[j][1]) + ")"] += 1

            elif sample[i] >= int_list[j][0] and sample[i] <= int_list[j][1] and j == len(int_list)-1:
                    freq_table["[" + str(int_list[j][0]) + "; " + str(int_list[j][1]) + "]"] += 1
        
    int_list_values = list()
    for key in freq_table:
        int_list_values.append(int(freq_table[key]))

    intr = list(freq_table.keys())

    centered_int = list()
    for intr in int_list:
        centered_int.append(round(((intr[0] + intr[1])/2), 3))

    freq_table_disc = dict()
    x = list(set(sample))
    for num in x:
        freq_table_disc[num] = sample.count(num)

    result = list()

    x = [0, 1]
    y = [1-p, p]

    result.append(x)
    result.append(y)

    plt.vlines(x, 0, y, linestyles='dashed')
    plt.scatter(x, y, zorder = 2)
    plt.show()

    mean = np.mean(sample)
    result.append(mean)

    moda = list(mode(freq_table_disc).keys())
    result.append(moda)

    med = statistics.median(sample)
    result.append(med)

    ro = max(sample) - min(sample)
    result.append(ro)
    
    deviation = dev(freq_table_disc)
    result.append(deviation)

    variansa = dev(freq_table_disc) / (len(sample)-1)
    result.append(variansa)

    standart = math.sqrt(variansa)
    result.append(standart)

    variation = standart / np.mean(sample)

    asym = st.skew(sample)
    result.append(asym)

    ex = st.kurtosis(sample)
    result.append(ex)

    return result

test()