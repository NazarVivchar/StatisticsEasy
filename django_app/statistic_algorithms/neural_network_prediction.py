from sklearn import neural_network
import numpy as np
from copy import deepcopy
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
def dnn_prediction(X,Y):
    x = []

    x.append((X[len(X) - 1] + 1))
    predictor = neural_network.MLPRegressor(hidden_layer_sizes=(50),activation='relu',max_iter=100)
    for i in range(Y.shape[1]-5):
        training_values = np.array([[Y[0][y_i] for y_i in range(i,i+5)]])
        result = np.array([[Y[0][i+5]]])
        predictor.fit(training_values,result)
    for i in range(5):

        n = Y.shape[1]

        testing = [Y[0][y_i] for y_i in range(Y.shape[1]-5,Y.shape[1])]
        inpt = np.array([testing])
        prediction = predictor.predict(
                inpt
                )

        tmp = []
        for i in range(Y.shape[1]):
            tmp.append(Y[0][i])


        tmp.append(prediction[0])

        Y = np.array([[*tmp[-5:-1]]])
        np.round(Y)
        while len(x)!= len(Y[0]):
            x.append(x[len(x)-1]+1)


    return x, Y[0]


