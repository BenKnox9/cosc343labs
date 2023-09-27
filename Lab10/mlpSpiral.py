from helper import *
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

X, y = load_spiral()
# y = y[:, 0]

numEpochs = 2000

mlp = MLPClassifier(hidden_layer_sizes=(16, 64), activation="logistic", max_iter=numEpochs,
                   learning_rate_init=0.1, learning_rate="adaptive", solver='sgd', tol=1e-5, n_iter_no_change=10000, verbose=True)

for epoch in range(numEpochs):
    mlp.partial_fit(X, y, classes=np.unique(y))
    if epoch % 20 == 0:
        plot_classified_regions(mlp, X, y, blocking=False, titleStr=print(f"epoch {epoch}"))
plot_classified_regions(mlp, X, y, blocking=True, titleStr=print(f"epoch {epoch}"))

