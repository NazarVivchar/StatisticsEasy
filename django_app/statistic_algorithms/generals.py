import random
import matplotlib.pyplot as plt
import math
import prettytable


def read(file) -> dict:
    keys = file.readline().split(' ')
    values = file.readline().split(' ')
    dict_values = {}
    for i in range(len(keys)):
        dict_values[int(keys[i])] = int(values[i])
    return dict_values


# des = input("Ви хочете зчитати з файлу(y/n): ")
des = 'y'

mydict = {}
discrete = []

if des.lower() == "y":
    mydict = read(open("TextFile1.txt", 'r'))
    size = sum(list(mydict.values()))
    for i in mydict.keys():
        discrete += [i] * mydict[i]
else:
    # amount = int(input("Введіть об'єм вибірки: "))
    # amount = 25
    # discrete = [random.randrange(0,15) for y in range(amount)]
    # discrete = [0,1,2,5,0,1,3,0,1,5,4,0,3,3,2,1,4,0,0,2,3,4,0,3,1]
    # discrete = [0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,3,3,3,3,3,4,4,5,5,6]
    myset = set(discrete)
    myset = sorted(myset)
    for i in myset:
        mydict[i] = discrete.count(i)

print("Дискретна вибірка: ", discrete)
print("--------------------------------------------------------------------------")

sort_discrete = discrete
sort_discrete.sort()
print("Варіаційний ряд: ", sort_discrete)
print("--------------------------------------------------------------------------")

print('Статистичний розподіл варіанти: ')
print('\t\t\t\t' + "xi : ni")
for i in mydict:
    print('\t\t\t\t ' + str(i) + " : " + str(mydict[i]))
print("--------------------------------------------------------------------------")

n = 0
numberofitems = []
for i in mydict.values():
    numberofitems.append(i)
    n += i

print("n = ", n)
print("--------------------------------------------------------------------------")

maxi = 0
mode = []
for k, v in mydict.items():
    if maxi < v:
        maxi = v
for k, v in mydict.items():
    if v == maxi:
        mode.append(k)
print("Мода: ", mode)
print("--------------------------------------------------------------------------")

mod = n % 2
if mod > 0:
    me = (len(sort_discrete) // 2) + 1
    print('Mедіана = ', sort_discrete[me - 1])
else:
    me = (n // 2)
    print('Mедіана = ', (sort_discrete[me - 1] + sort_discrete[me]) / 2)
print("--------------------------------------------------------------------------")

summ = 0
for i in mydict.keys():
    summ += i * mydict[i]
mean = summ / n
print('Середнє арифметичне = ', mean)
print("--------------------------------------------------------------------------")

dev = 0
for i in mydict.keys():
    dev += mydict[i] * (i - mean) * (i - mean)

print('\t\t\t\t' + "xi : ni : ni*дев")
for i in mydict:
    print('\t\t\t\t ' + str(i) + " : " + str(mydict[i]) + " : " + str(mydict[i] * (i - mean) * (i - mean)))
print('Девіація = ', dev)
print("--------------------------------------------------------------------------")

variantsa = dev / (n - 1)
print("Варіанса = ", variantsa)
print("--------------------------------------------------------------------------")

s = math.sqrt(variantsa)
print("Стандарт = ", s)
print("--------------------------------------------------------------------------")

keys = list(mydict.keys())
rozmah = keys[-1] - keys[0]
print("Розмах = ", rozmah)
print("--------------------------------------------------------------------------")

var = s / mean
print("Варіація = ", var)
print("--------------------------------------------------------------------------")

# kratnist = 100 / n
# alfa = int(input("Введіть порядок квантиля: "))
# if alfa % kratnist == 0:
#    kvantyl = (n*alfa)/100
#    print("Квантиль порядку {0} = {1}".format(alfa, sort_discrete[int(kvantyl)-1]))
# else:
#    print("Квантиль не кратний")
# print("--------------------------------------------------------------------------")


kvartyl1 = n / 4
kvartyl2 = (2 * n) / 4
kvartyl3 = (3 * n) / 4

if kvartyl1.is_integer():
    print("Квартиль q1 = ", sort_discrete[int(kvartyl1) - 1])
else:
    print("Квартиль q1 не існує")
if kvartyl2.is_integer():
    print("Квартиль q2 =", sort_discrete[int(kvartyl2) - 1])
else:
    print("Квартиль q2 не існує")
if kvartyl3.is_integer():
    print("Квартиль q3 = ", sort_discrete[int(kvartyl3) - 1])
else:
    print("Квартиль q3 не існує")
print("--------------------------------------------------------------------------")


def count_decel(decel, numb):
    if decel.is_integer():
        print("Децель D{0} = {1}".format(numb, sort_discrete[int(decel) - 1]))


decel1 = n / 10
decel2 = (2 * n) / 10
decel3 = (3 * n) / 10
decel4 = (4 * n) / 10
decel5 = (5 * n) / 10
decel6 = (6 * n) / 10
decel7 = (7 * n) / 10
decel8 = (8 * n) / 10
decel9 = (9 * n) / 10

count_decel(decel1, 1)
count_decel(decel2, 2)
count_decel(decel3, 3)
count_decel(decel4, 4)
count_decel(decel5, 5)
count_decel(decel6, 6)
count_decel(decel7, 7)
count_decel(decel8, 8)
count_decel(decel9, 9)
print("--------------------------------------------------------------------------")


def count_centel(centel, numb):
    if centel.is_integer():
        print("Центель C{0} = {1}".format(numb, sort_discrete[int(centel) - 1]))


centeli = []
for i in range(1, 100):
    count = (i * n) / 100
    centeli.append((count))

for i in range(0, len(centeli)):
    count_centel(centeli[i], i + 1)
print("--------------------------------------------------------------------------")


def count_milil(milil, numb):
    if milil.is_integer():
        print("Міліля M{0} = {1}".format(numb, sort_discrete[int(milil) - 1]))


milili = []
for i in range(1, 1000):
    count = (i * n) / 1000
    milili.append((count))

for i in range(0, len(milili)):
    count_milil(milili[i], i + 1)
print("--------------------------------------------------------------------------")

values = list(mydict.values())
results = []
moments = []
# с = int(input("Введіть константу моменту: "))
c = mean
if c == 0:
    for k in range(2, 5):
        for i in range(0, len(mydict)):
            results.append(values[i] * math.pow(keys[i], k))
        moments.append(sum(results) / n)
        # for i in results:
        #    print(round(i, 3), end ="  ")
        result = sum(results) / n
        print("\nМомент при С = {0} та при k = {1} = {2}".format(round(c, 2), round(k, 2), round(result, 3)))
        results.clear()
elif c == mean:
    for k in range(2, 5):
        for i in range(0, len(mydict)):
            results.append(values[i] * math.pow(keys[i] - mean, k))
        moments.append(sum(results) / n)
        # for i in results:
        #    print(round(i, 3), end ="  ")
        result = sum(results) / n
        print("\nМомент при С = {0} та при k = {1} = {2}".format(round(c, 2), round(k, 2), round(result, 3)))
        results.clear()
else:
    for k in range(2, 5):
        for i in range(0, len(mydict)):
            results.append(values[i] * math.pow(keys[i] - c, k))
        moments.append(sum(results) / n)
        # for i in results:
        #    print(round(i, 3), end ="  ")
        result = sum(results) / n
        print("\nМомент при С = {0} та при k = {1} = {2}".format(round(c, 2), round(k, 2), round(result, 3)))
        results.clear()
for i in range(len(moments)):
    print("Момент " + str(i + 1) + " = " + str(round(moments[i], 3)))
print("\n--------------------------------------------------------------------------")

asymmetry = moments[1] / math.pow(moments[0], 1.5);
print("Асиметрія = ", asymmetry)
print("--------------------------------------------------------------------------")

excess = (moments[2] / math.pow(moments[0], 2)) - 3;
print("Ексцес = ", excess)
print("--------------------------------------------------------------------------")


def getFunction(keys: list, values: list, prob: list) -> dict:
    function_values = [[0, " x < {0}".format(keys[0])]]
    previous_value = 0
    for i in range(len(keys)):
        if (i != len(keys) - 1):
            tmp_i = i + 1
            function_values.append([round(previous_value + prob[i], 2), " {0} <= x < {1}".format(keys[i], keys[tmp_i])])
        else:
            function_values.append([round(previous_value + prob[i], 2), " x >= {0}".format(keys[i])])
        previous_value += prob[i]
    return function_values


count_values = []
size = sum(list(mydict.values()))
for i in mydict.keys():
    count_values.append(mydict[i] / size)

print("Функція емпіричного розподілу")
func_numb = getFunction(list(mydict.keys()), list(mydict.values()), count_values)
func_values = [i[0] for i in func_numb]

for i in func_numb:
    print(str(i[0]) + " ," + i[1])

# полігон частот дискретної вибірки
plt.figure(figsize=(12, 6))
graphic1 = plt.subplot(121)
plt.grid(True)
graphic1.plot(mydict.keys(), numberofitems)
for i in mydict.keys():
    plt.plot([i, i], [0, mydict[i]], 'k-')
plt.title('Полігон частот', fontsize=30)
plt.xlabel('ni')
plt.ylabel('xi')

# графік функції емпіричного розподілу

graphic2 = plt.subplot(122)
plt.grid(True)
plt.title('Емпіричний розподілу', fontsize=25)
X = list(mydict.keys()) * 2
Y = list(func_values) * 2
Y.remove(0)
Y.remove(1)
Y.sort()
X.sort()
graphic2.plot(X, Y, 'bo')
for i in range(len(X)):
    if (i == 0):
        graphic2.plot([X[i], X[i] - X[i] * 0.2 if (X[i] != 0) else X[i] - 1], [Y[i], Y[i]], 'k-')
    elif (i == len(X) - 1):
        graphic2.plot([X[i], X[i] + X[i] * 0.1], [Y[i], Y[i]], 'k-')
    else:
        graphic2.plot([X[i], X[i + 1]], [Y[i], Y[i]], 'k-')

# plt.show()


print(
    "-----------------------------------Неперервна статистична змінна-------------------------------------------------")

# des = input("Ви хочете зчитати з файлу(y/n): ")
des = 'y'
uninterrupted = []

if des.lower() == "y":

    with open('TextFile2.txt') as f:
        s = f.readline().replace(',', '')
        s = str(s)
        for i in range(len(s)):
            s[i].replace('[', '')
            s[i].replace(']', '')
            s[i].replace(' ', '')
        newstr = ''.join((ch if ch in '0123456789.-' else ' ') for ch in s)
        listOfNumbers = [float(i) for i in newstr.split()]

        numb = []
        for val in f.read().split():
            numb.append(int(val))

        f.close()

    intervals = [listOfNumbers[i * 2:(i + 1) * 2] for i in range((len(listOfNumbers) + 2 - 1) // 2)]

    n = sum(numb)
    print("n = ", n)
    print("--------------------------------------------------------------------------")

    r = math.ceil(math.log2(n))
    print("r = ", r)
    print("--------------------------------------------------------------------------")

    print(intervals[-1][-1])
    rozmah = intervals[-1][-1] - intervals[0][0]
    print("Розмах = ", rozmah)
    print("--------------------------------------------------------------------------")

    h = rozmah / r
    print("Крок = ", h)
    print("--------------------------------------------------------------------------")

    with open('TextFile3.txt') as f:
        uninterrupted = []
        for val in f.read().split():
            uninterrupted.append(float(val))

    uninterrupted_count = []
    count = 0
    start = 0
    for interval in intervals:
        for j in range(start, len(uninterrupted)):
            if ((uninterrupted[j] >= interval[0] and uninterrupted[j] < interval[1]) or (
                    j == len(uninterrupted) - 1) and
                    intervals.index(interval) == len(intervals) - 1):
                count += 1
            else:
                start = j
                break
        uninterrupted_count.append(count)
        count = 0

else:
    # uninterrupted = [round(random.uniform(5.5,11),1) for i in range(30)]
    uninterrupted = [2.7, 3.2, 1.8, 1.0, 2.1, 2.5, 1.7, 1.2, 3.7, 1.8, 2.4, 1.9, 2.3, 1.8, 2.6, 1.9, 2.2, 2.9, 0.8, 1.6,
                     1.3, 3.1, 0.7, 1.0, 1.9]
    print("Неперервна вибірка: ", uninterrupted)
    print("--------------------------------------------------------------------------")

    uninterrupted.sort()
    print("Посортована неперервна вибірка: ", uninterrupted)
    print("--------------------------------------------------------------------------")

    n = len(uninterrupted)
    print("n = ", n)
    print("--------------------------------------------------------------------------")

    r = math.ceil(math.log2(n))
    print("r = ", r)
    print("--------------------------------------------------------------------------")

    rozmah = uninterrupted[-1] - uninterrupted[0]
    print("Розмах = ", rozmah)
    print("--------------------------------------------------------------------------")

    h = rozmah / r
    print("Крок = ", h)
    print("--------------------------------------------------------------------------")

    intervals = [[uninterrupted[0], round(uninterrupted[0] + h, 3)]]
    for i in range(0, r - 1):
        if (i != r - 2):
            intervals.append([intervals[i][1], round(intervals[i][1] + h, 3)])
        else:
            intervals.append([intervals[i][1], round(intervals[i][1] + h, 3)])

    print(intervals)

    uninterrupted_count = []
    count = 0
    start = 0
    for interval in intervals:
        for j in range(start, len(uninterrupted)):
            if ((uninterrupted[j] >= interval[0] and uninterrupted[j] < interval[1]) or (
                    j == len(uninterrupted) - 1) and
                    intervals.index(interval) == len(intervals) - 1):
                count += 1
            else:
                start = j
                break
        uninterrupted_count.append(count)
        count = 0

uninterrupted_prob = []
for i in uninterrupted_count:
    uninterrupted_prob.append(round(i / n, 3))

avarage_values = []
for i in intervals:
    avarage_values.append(round((i[1] - i[0]) / 2 + i[0], 3))

uninterrupted_table = prettytable.PrettyTable()
uninterrupted_table.header = False
uninterrupted_table.add_row(['  '] + intervals)
uninterrupted_table.add_row(['ni'] + uninterrupted_count)
uninterrupted_table.add_row(['xi'] + avarage_values)

print(uninterrupted_table)

summ = 0
for i in range(len(uninterrupted_count)):
    summ += uninterrupted_count[i] * avarage_values[i]
mean = summ / n
print('Середнє арифметичне = ', mean)
print("--------------------------------------------------------------------------")

maximum = max(uninterrupted_count)
for i in range(r):
    if uninterrupted_count[i] == maximum:
        print("Мода: ", intervals[i])
print("--------------------------------------------------------------------------")

mod = n % 2
if mod > 0:
    me = (n // 2) + 1
    print('Mедіана = ', uninterrupted[me - 1])
else:
    me = (n // 2)
    print('Mедіана = ', (uninterrupted[me - 1] + uninterrupted[me]) / 2)
print("--------------------------------------------------------------------------")

devi = []
dev = 0
for i in range(r):
    temp = round(uninterrupted_count[i] * pow(avarage_values[i] - mean, 2), 2)
    dev += temp
    devi.append(temp)

deviatsiya = prettytable.PrettyTable()
deviatsiya.header = False
deviatsiya.add_row(['ni*(xi - mean)^2'] + devi)
print(deviatsiya)
print('Девіація = ', dev)
print("--------------------------------------------------------------------------")

variantsa = dev / (n - 1)
print("Варіанса = ", variantsa)
print("--------------------------------------------------------------------------")

s = math.sqrt(variantsa)
print("Стандарт = ", s)
print("--------------------------------------------------------------------------")

var = s / mean
print("Варіація = ", var)
print("--------------------------------------------------------------------------")

# kratnist = 100 / n
# alfa = int(input("Введіть порядок квантиля: "))
# if alfa % kratnist == 0:
#    kvantyl = (n*alfa)/100
#    print("Квантиль порядку {0} = {1}".format(alfa, uninterrupted[int(kvantyl)-1]))
# else:
#    print("Квантиль не кратний")
# print("--------------------------------------------------------------------------")


kvartyl1 = n / 4
kvartyl2 = (2 * n) / 4
kvartyl3 = (3 * n) / 4

if kvartyl1.is_integer():
    print("Квартиль q1 = ", uninterrupted[int(kvartyl1) - 1])
else:
    print("Квартиль q1 не існує")
if kvartyl2.is_integer():
    print("Квартиль q2 =", uninterrupted[int(kvartyl2) - 1])
else:
    print("Квартиль q2 не існує")
if kvartyl3.is_integer():
    print("Квартиль q3 = ", uninterrupted[int(kvartyl3) - 1])
else:
    print("Квартиль q3 не існує")
print("--------------------------------------------------------------------------")


def count_decel(decel, numb):
    if decel.is_integer():
        print("Децель D{0} = {1}".format(numb, uninterrupted[int(decel) - 1]))


decel1 = n / 10
decel2 = (2 * n) / 10
decel3 = (3 * n) / 10
decel4 = (4 * n) / 10
decel5 = (5 * n) / 10
decel6 = (6 * n) / 10
decel7 = (7 * n) / 10
decel8 = (8 * n) / 10
decel9 = (9 * n) / 10

count_decel(decel1, 1)
count_decel(decel2, 2)
count_decel(decel3, 3)
count_decel(decel4, 4)
count_decel(decel5, 5)
count_decel(decel6, 6)
count_decel(decel7, 7)
count_decel(decel8, 8)
count_decel(decel9, 9)
print("--------------------------------------------------------------------------")


def count_centel(centel, numb):
    if centel.is_integer():
        print("Центель C{0} = {1}".format(numb, uninterrupted[int(centel) - 1]))


centeli = []
for i in range(1, 100):
    count = (i * n) / 100
    centeli.append((count))

for i in range(0, len(centeli)):
    count_centel(centeli[i], i + 1)
print("--------------------------------------------------------------------------")


def count_milil(milil, numb):
    if milil.is_integer():
        print("Міліля M{0} = {1}".format(numb, uninterrupted[int(milil) - 1]))


milili = []
for i in range(1, 1000):
    count = (i * n) / 1000
    milili.append((count))

for i in range(0, len(milili)):
    count_milil(milili[i], i + 1)
print("--------------------------------------------------------------------------")

myset = set(uninterrupted)
myset = sorted(myset)
mydict = {}

for i in myset:
    mydict[i] = uninterrupted.count(i)

keys = list(mydict.keys())
values = list(mydict.values())
results = []
moments = []
# с = int(input("Введіть константу моменту: "))
c = mean
if c == 0:
    for k in range(2, 5):
        for i in range(0, len(mydict)):
            results.append(values[i] * math.pow(keys[i], k))
        moments.append(sum(results) / n)
        # for i in results:
        #    print(round(i, 3), end ="  ")
        result = sum(results) / n
        print("\nМомент при С = {0} та при k = {1} = {2}".format(c, k, round(result, 3)))
        results.clear()
elif c == mean:
    for k in range(2, 5):
        for i in range(0, len(mydict)):
            results.append(values[i] * math.pow(keys[i] - mean, k))
        moments.append(sum(results) / n)
        # for i in results:
        #    print(round(i, 3), end ="  ")
        result = sum(results) / n
        print("\nМомент при С = {0} та при k = {1} = {2}".format(c, k, round(result, 3)))
        results.clear()
else:
    for k in range(2, 5):
        for i in range(0, len(mydict)):
            results.append(values[i] * math.pow(keys[i] - c, k))
        moments.append(sum(results) / n)
        # for i in results:
        #    print(round(i, 3), end ="  ")
        result = sum(results) / n
        print("\nМомент при С = {0} та при k = {1} = {2}".format(c, k, round(result, 3)))
        results.clear()
for i in range(len(moments)):
    print("Момент " + str(i + 1) + " = " + str(round(moments[i], 3)))
print("\n--------------------------------------------------------------------------")

asymmetry = moments[1] / math.pow(moments[0], 1.5);
print("Асиметрія = ", asymmetry)
print("--------------------------------------------------------------------------")

excess = (moments[2] / math.pow(moments[0], 2)) - 3;
print("Ексцес = ", excess)
print("--------------------------------------------------------------------------")

uninterrupted_function = [0]
for i in range(len(uninterrupted_prob)):
    uninterrupted_function.append(uninterrupted_prob[i] + uninterrupted_function[i])

edges = [intervals[0][0]]
for i in intervals:
    edges.append(i[1])

plt.figure(figsize=(12, 6))
uninterrupted_diagram = plt.subplot(1, 2, 1)
plt.title('Гістограма', fontsize=30)
uninterrupted_diagram.hist(uninterrupted, len(intervals), color='magenta', ec='black')

uninterrupted_function_graph = plt.subplot(1, 2, 2)
uninterrupted_function_graph.plot(avarage_values, uninterrupted_count, 'b-', linewidth=5)

plt.show()





