from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from django_app.models import ImageFile
from shutil import copyfile
import pandas as pd
def class_to_color(features):
    classes =[]
    for i in features:
        if i == 'Europe.':
            classes.append('green')
        elif i == 'US.':
            classes.append('black')
        else:
            classes.append('blue')
    return classes


def main(row_argument1 = 'weightlbs',row_argument2= 'year', row_feature='brand',filename = 'clastering.csv'):
    data = pd.read_csv(filename)
    print(data)
    x = data[row_argument1]
    y = data[row_argument2].values
    map(float,x)
    map(int, y)

    a =[]
    for i in range(len(x)):
        a.append([x[i],y[i]])
    points = np.array(a)
    features = np.array(data[row_feature].values)
    classes = class_to_color(features)


    plt.scatter(points[:,0],points[:,1], c=classes, cmap='viridis')
    plt.savefig('hierarcial_preview.png')
    copyfile('./hierarcial_preview.png', 'media/hierarcial_preview.png')
    ImageFile.objects.create(image='hierarcial_preview.png')
    plt.close()

    dendrogram = sch.dendrogram(sch.linkage(points, method='ward'))

    plt.savefig('hierarcial_dendrogram.png')
    copyfile('./hierarcial_dendrogram.png', 'media/hierarcial_dendrogram.png')
    ImageFile.objects.create(image='hierarcial_dendrogram.png')

    plt.close()
    hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')

    # save clusters for chart
    y_hc = hc.fit_predict(points)

    plt.scatter(points[y_hc == 0, 0], points[y_hc == 0, 1], s=100, c='red')

    plt.scatter(points[y_hc == 1, 0], points[y_hc == 1, 1], s=100, c='black')

    plt.scatter(points[y_hc == 2, 0], points[y_hc == 2, 1], s=100, c='blue')



    plt.savefig('hierarcial_result.png')
    copyfile('./hierarcial_result.png', 'media/hierarcial_result.png')
    ImageFile.objects.create(image='hierarcial_result.png')
    print(1)



