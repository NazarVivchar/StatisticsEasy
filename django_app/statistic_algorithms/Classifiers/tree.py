# import matplotlib.pyplot as plt
# from sklearn import datasets
from sklearn import tree

classifier = tree.DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
                                         max_features=None, max_leaf_nodes=None,
                                         min_impurity_decrease=0.0, min_impurity_split=None,
                                         min_samples_leaf=1, min_samples_split=2,
                                         min_weight_fraction_leaf=0.0, presort=False, random_state=None,
                                         splitter='best')

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
##a=[[1,2,3,4,5,6,7,8,9,'Ivan'],
##   [1,2,3,4,5,6,7,7,5,'Petro'],
##   [1,2,3,4,5,6,7,8,9,'Ivan'],
##   [11,2,3,1,5,6,7,8,100,'Marta'],
##   [1,2,3,4,5,6,7,8,5,'Petro'],
##   [1,2,3,3,5,6,7,8,100,'Marta'],
##   [51,2,3,4,5,6,11,8,100,'Marta'],
##   [1,2,3,4,5,6,7,8,5,'Petro'],
##   [1,12,3,3,5,6,7,8,9,'Ivan'],
##   [1,2,3,4,0,6,7,8,5,'Petro'],
##   [1,2,3,6,5,6,7,8,9,'Ivan']]
##fit(a)
##print(predict([1,2,3,4,5,8,7,8,100]))
##def show_tree():
##    import graphviz
##    dot_data = tree.export_graphviz(classifier, out_file=None)
##    graph = graphviz.Source(dot_data)
##    graph.render("points")
##    dot_data = tree.export_graphviz(classifier, out_file=None,
##                        feature_names=None,
##                        class_names=opt_dict.values(),
##                        filled=True, rounded=True,
##                        special_characters=True)
##    graph = graphviz.Source(dot_data)
##    graph
