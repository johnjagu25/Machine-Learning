
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn import linear_model 
import pandas as pd

import numpy as np
from sklearn.datasets import load_boston,load_diabetes
import matplotlib.pyplot as plt

class LinearRegression():
    def __init__(self, X, y, alpha=0.005, n_iter=1000):

        self.alpha = alpha
        self.n_iter = n_iter
        self.n_samples,self.n_features = X.shape        
        self.params = np.zeros((self.n_features + 1, 1))
        self.coef_ = None
        self.intercept_ = None

    def fit(self,X,y):
        self.X = np.hstack((np.ones(
            (self.n_samples, 1)), (X - np.mean(X, 0)) / np.std(X, 0)))
        self.y = y[:, np.newaxis]
        for i in range(self.n_iter):
            self.params = self.params - (self.alpha/self.n_samples) * \
            self.X.T @ (self.X @ self.params - self.y)

        self.intercept_ = self.params[0]
        self.coef_ = self.params[1:]

        return self

    def score(self, X=None, y=None):
        if X is None:
            X = self.X
        else:
            n_samples = np.size(X, 0)
            X = np.hstack((np.ones(
                (n_samples, 1)), (X - np.mean(X, 0)) / np.std(X, 0)))

        if y is None:
            y = self.y
        else:
            y = y[:, np.newaxis]

        y_pred = X @ self.params
        score = 1 - (((y - y_pred)**2).sum() / ((y - y.mean())**2).sum())

        return score

    def predict(self, X):
        n_samples = np.size(X, 0)
        y = np.hstack((np.ones((n_samples, 1)), (X-np.mean(X, 0)) \
                            / np.std(X, 0))) @ self.params
        return y

    def get_params(self):

        return self.params
def main():
    dataset = load_boston()
    X = dataset.data
    y = dataset.target
    X_train, X_test, y_train, y_test = train_test_split(\
                X, y, test_size=0.3)
    n_features = X.shape[1]
    params = np.zeros((n_features,1))
    reg = LinearRegression(X_train, y_train)
    reg.fit(X_train,y_train)
    print(reg.score(X_test, y_test))

if __name__ == "__main__":
    main()
