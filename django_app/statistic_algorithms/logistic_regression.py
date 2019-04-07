import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn import metrics
import seaborn as sns
import numpy as np
from ..models import ImageFile
from shutil import copyfile



def func(file, pred_row):
    train = pd.read_csv(file)
    X_train, X_test, y_train, y_test = train_test_split(train.drop(pred_row, axis=1),
                                                        train[pred_row], test_size=0.30,
                                                        random_state=101)
    logmodel = LogisticRegression()
    logmodel.fit(X_train, y_train)
    predictions = logmodel.predict(X_test)
    cnf_matrix = metrics.confusion_matrix(y_test, predictions)
    print(cnf_matrix)
    class_names = [0, 1]  # name  of classes
    fig, ax = plt.subplots()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names)
    plt.yticks(tick_marks, class_names)
    sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu", fmt='g')
    ax.xaxis.set_label_position("top")
    plt.tight_layout()
    plt.title('Confusion matrix', y=1.1)

    plt.savefig('logistc_result.png')
    copyfile('./logistc_result.png','media/logistc_result.png')
    ImageFile.objects.create(image='media/logistc_result.png')
    return X_test.head(), y_test[0:6], predictions[0:6], classification_report(y_test, predictions)

