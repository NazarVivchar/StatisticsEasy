# import matplotlib.pyplot as plt
# from sklearn import datasets
from sklearn import svm

classifier = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
                     decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
                     max_iter=-1, probability=False, random_state=None, shrinking=True,
                     tol=0.001, verbose=False)

opt_dict = {}
features = []
targets = []


def fit(data):
    opt_dict.clear()
    features.clear()
    targets.clear()
    i = 0
    names = []

    for x in data:
        features.append(x[:-1])
        names.append(x[-1])
    temp = list(set(names))

    for j in range(len(temp)):
        opt_dict[i] = temp[j]
        i += 1

    for i in names:
        for alies in opt_dict.keys():
            if i == opt_dict[alies]:
                targets.append(alies)
                break

    classifier.fit(features, targets)


def predict(values: list):
    result_list = classifier.predict([values])
    return opt_dict[result_list[0]]


# test
# a = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 'Ivan'],
#      [1, 2, 3, 4, 5, 6, 7, 7, 5, 'Petro'],
#      [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Ivan'],
#      [11, 2, 3, 1, 5, 6, 7, 8, 100, 'Marta'],
#      [1, 2, 3, 4, 5, 6, 7, 8, 5, 'Petro'],
#      [1, 2, 3, 3, 5, 6, 7, 8, 100, 'Marta'],
#      [51, 2, 3, 4, 5, 6, 11, 8, 100, 'Marta'],
#      [1, 2, 3, 4, 5, 6, 7, 8, 5, 'Petro'],
#      [1, 12, 3, 3, 5, 6, 7, 8, 9, 'Ivan'],
#      [1, 2, 3, 4, 0, 6, 7, 8, 5, 'Petro'],
#      [1, 2, 3, 6, 5, 6, 7, 8, 9, 'Ivan']]
# fit(a)
# print(predict([1, 2, 3, 4, 5, 8, 7, 8, 100]))
