import math

# Функції для обчислення деяких характеристик

def mode(freq_table):
    result = dict()

    for key in freq_table:
        if freq_table[key] == max(freq_table.values()):
            result[key] = float(freq_table[key])

    return result

def dev(freq_table):
    res = 0
    avg = 0
    length = 0

    for x in freq_table:
        avg += (x * freq_table[x])
        length += freq_table[x]

    avg /= length

    for x in freq_table:
        res +=  freq_table[x] * (x - avg)**(2)
    return res

def stdev(nums):
    diffs = 0
    avg = sum(nums)/len(nums)
    for n in nums:
        diffs += (n - avg)**(2)
    return (diffs/(len(nums)-1))**(0.5)

def r(sample):
    res = 0
    n = len(sample)

    while not (n > math.pow(2,res) and n <= math.pow(2, res+1)):
        res += 1

    return res

def centr_mean(centr_freq):
    res = 0
    for key in centr_freq:
        res += float(key) * centr_freq[key]

    return res / sum(centr_freq.values())