import numpy as np
import matplotlib.pyplot as plt

class ExerciseOne:

    def __init__(self, learning_rate=0.01, max_iter=100, verbose=False):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.verbose = verbose
        self.W = None
        self.b = None
        self.class_labels = None
        self._trained = False

    def doStuff(self):
        X = np.array([[-1, -1],
                      [-1, 1],
                      [1, -1],
                      [1, 1]]).astype('float32')

        y = np.array([0,
                      0,
                      0,
                      1]).astype('uint8')

        plt.scatter(X[:3, 0], X[:3, 1], c='red')
        plt.scatter(X[3, 0], X[3, 1], c='blue')
        plt.xlabel('x 1')
        plt.ylabel('x 2')
        plt.show()

        N, D = np.shape(X)
        K = 1
        Y = np.expand_dims(y, axis=1)

        self.W = np.random.randn(D, K)
        self.b = np.random.randn(K)

        for i in range(self.max_iter):
            firstThing = np.matmul(X, self.W) + self.b
            yHat = self.evaluateYhat(firstThing)
            error = Y - yHat

            # changeWithWeight = error * self.learning_rate
            self.W += np.matmul(X.T, error) * self.learning_rate
            self.b += np.sum(error) * self.learning_rate


    def evaluateYhat(self, input):
        return np.where(input > 0, 1, 0)

if __name__ == "__main__":
    exercise = ExerciseOne()
    exercise.doStuff()
