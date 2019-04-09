import numpy
import scipy.stats as st


def predict(alpha, beta, x_i):
    return beta*x_i + alpha


def least_squers_fit(x,y):
    beta = numpy.corrcoef(x,y)[0,1]*numpy.std(y)/numpy.std(x)
    
    alpha = numpy.mean(y) - beta*numpy.mean(x)
    
    return alpha, beta

# def main(test_points, new_point):
    # x = [i for i,_ in test_points ]
    # y = [i for _, i in test_points]
    # alpha, beta = least_squers_fit(x,y)
    # prediction = predict(alpha, beta, new_point)
    # return alpha, beta, prediction

