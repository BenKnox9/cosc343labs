from helper import *
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# X, y = load_spiral()
X, y = load_mnist()

X = np.reshape(X, (70000, 784))
# y = y[:, 0]

X_train = X[:60000]
X_test = X[60000:]
y_train = y[:60000]
y_test = y[60000:]


numEpochs = 100

mlp = MLPClassifier(hidden_layer_sizes=(100, 200), activation="identity", max_iter=numEpochs,
                    learning_rate_init=0.0001, solver='sgd', tol=1e-5, n_iter_no_change=10000, verbose=True)



mlp.fit(X_train, y_train)

test_accuracy =mlp.score(X_test, y_test)
print("Test accuracy: %f" % (test_accuracy))


