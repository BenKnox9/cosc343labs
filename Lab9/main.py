# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

from helper import *
from PolynomialRegressor import PolynomialRegressor
from PolynomialClassifier import PolynomialClassifier
import matplotlib.pyplot as plt


def doit():
    X, y = load_reg1dataset()
    plt.scatter(X, y, c='b')

    k = 1
    Xb = PolynomialRegressor.input_to_poly_features(X, degree=k)

    w = np.dot(np.dot(np.linalg.inv(np.dot(Xb.T, Xb)), Xb.T), y)

    xmin = np.min(X)
    xmax = np.max(X)
    xtest = np.linspace(xmin, xmax, 200)
    Xtest = np.expand_dims(xtest, axis=1)

    Xbtest = PolynomialRegressor.input_to_poly_features(Xtest, degree=k)
    ytest = np.dot(Xbtest, w)
    plt.plot(Xtest, ytest, c='r')

    plt.show()

def doitTwo():
    X, y = load_reg1dataset()

    model = PolynomialRegressor(degree=1, learning_rate=0.1, max_iter=10)

    for epoch in range(100):
        model.fit(X, y)
        model.plot_function(X, y, titleStr="Epoch %d" % ((epoch + 1) * model.max_iter))

    plt.ioff()
    plt.show()

def doitThree():
    X, y = load_xor()

    model = PolynomialClassifier(degree=1, learning_rate=0.1, max_iter=10)

    for epoch in range(100):
        model.fit(X, y)
        model.plot_classified_regions(X, y, titleStr="Epoch %d" % ((epoch + 1) * model.max_iter))

    plt.ioff()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    doitThree()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
