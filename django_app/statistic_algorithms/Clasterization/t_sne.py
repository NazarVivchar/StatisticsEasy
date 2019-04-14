from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from django_app.models import ImageFile
from shutil import copyfile
def main():
    iris_df = datasets.load_iris()


    x_axis = iris_df.data[:, 0]  # Sepal Length
    y_axis = iris_df.data[:, 1]  # Sepal Width

    # Построение
    plt.xlabel(iris_df.feature_names[0])
    plt.ylabel(iris_df.feature_names[1])
    plt.scatter(x_axis, y_axis, c=iris_df.target)
    plt.savefig('t_sne_preview.png')
    copyfile('./t_sne_preview.png', 'media/t_sne_preview.png')
    ImageFile.objects.create(image='t_sne_preview.png')
    plt.close()
    iris_df = datasets.load_iris()

    # Определяем модель и скорость обучения
    model = TSNE(learning_rate=100)

    # Обучаем модель
    transformed = model.fit_transform(iris_df.data)

    # Представляем результат в двумерных координатах
    x_axis = transformed[:, 0]
    y_axis = transformed[:, 1]

    plt.scatter(x_axis, y_axis, c=iris_df.target)

    plt.savefig('t_sne_result.png')
    plt.close()
    copyfile('./t_sne_result.png', 'media/t_sne_result.png')
    ImageFile.objects.create(image='t_sne_result.png')