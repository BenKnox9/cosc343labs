from helper import *
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

X, y = load_reg1dataset()
y = y[:, 0]

numEpochs = 1000

mlp = MLPRegressor(hidden_layer_sizes=(100, 200), activation="identity", max_iter=numEpochs,
                   learning_rate_init=0.01, solver='sgd', tol=1e-5, n_iter_no_change=10000)

for epoch in range(numEpochs):
    mlp.partial_fit(X, y)
    plot_function(mlp, X, y, blocking=False, titleStr=f"EPOCH: {epoch}")

plot_function(mlp, X, y, blocking=True)
