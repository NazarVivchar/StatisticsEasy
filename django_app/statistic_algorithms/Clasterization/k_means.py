from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from django_app.models import ImageFile
from shutil import copyfile
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



    kmeans = KMeans(n_clusters=3)

    # fit kmeans object to data

    print(points)
    kmeans.fit(points)

    # print location of clusters learned by kmeans object
    print(kmeans.cluster_centers_)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], c ='red',cmap='viridis', s=[100,100,100])

    plt.savefig('k_means_preview.png')
    copyfile('./k_means_preview.png', 'media/k_means_preview.png')
    ImageFile.objects.create(image='k_means_preview.png')

    y_km = kmeans.fit_predict(points)

    plt.scatter(points[y_km == 0, 0], points[y_km == 0, 1], s=100, c='green')

    plt.scatter(points[y_km == 1, 0], points[y_km == 1, 1], s=100, c='black')

    plt.scatter(points[y_km == 2, 0], points[y_km == 2, 1], s=100, c='blue')

    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', cmap='viridis',
                s=[100, 100, 100])
    plt.legend(['USA', 'Japan', 'Europe'])

    plt.savefig('k_means_result.png')
    copyfile('./k_means_result.png', 'media/k_means_result.png')
    ImageFile.objects.create(image='k_means_result.png')


