import matplotlib.pyplot as plt
# from sklearn import datasets
from sklearn import linear_model

classifier = linear_model.SGDClassifier(alpha=0.0001, average=False, class_weight=None,
                                        early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
                                        l1_ratio=0.15, learning_rate='optimal', loss='hinge', max_iter=1000,
                                        n_iter=None, n_iter_no_change=5, n_jobs=None, penalty='l2',
                                        power_t=0.5, random_state=None, shuffle=True, tol=1e-3,
                                        validation_fraction=0.1, verbose=1, warm_start=False)

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


##test
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
