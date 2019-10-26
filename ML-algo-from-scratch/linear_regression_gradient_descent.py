
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn import linear_model 
import pandas as pd

import numpy as np
from sklearn.datasets import load_boston,load_diabetes
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge,Lasso
from sklearn.preprocessing import MinMaxScaler

class LinearRegression():
    def __init__(self, alpha=0.05, n_iter=1000, reg=lambda w : 0, lamb=0 , polyReg = False,lossfunc = lambda w : 0 ):

        self.alpha = alpha
        self.n_iter = n_iter      
        self.coef_ = None
        self.intercept_ = None
        self.cost = []
        self.polyReg = polyReg
        self.reg = reg
        self.lamb = lamb
        self.lossfunc =lossfunc

    def fit(self,X,y):
        self.n_samples,self.n_features = X.shape    
        
        if self.polyReg:
            self.params = np.zeros((self.n_features, 1))
            self.X = X            
        else:
            self.params = np.zeros((self.n_features + 1, 1))
            self.X = np.hstack((np.ones(
                (self.n_samples, 1)), (X - np.mean(X, 0)) / np.std(X, 0)))
            
        regularization = self.reg
        self.y = y[:, np.newaxis]
        for i in range(self.n_iter):            
            predictions = self.X @ self.params 
            self.mse = 0.5 * np.mean((y - predictions)**2) + self.lossfunc(self.params)
            self.params -= (regularization(self.params) * self.alpha/self.n_samples)+  (self.alpha/self.n_samples) * self.X.T @ (predictions - self.y)
      
        self.intercept_ = self.params[0]
        self.coef_ = self.params[1:]

        return self
    def mean_squared_error(self):
        return self.mse

    def score(self, X=None, y=None):

        n_samples = np.size(X, 0)
        X = np.hstack((np.ones((n_samples, 1)), (X - np.mean(X, 0)) / np.std(X, 0)))
        y = y[:, np.newaxis]
        y_pred = X @ self.params
        score = 1 - (((y - y_pred)**2).sum() / ((y - y.mean())**2).sum())

        return score

    def predict(self, X):
        n_samples = np.size(X, 0)
        if self.polyReg  :
            y = X @ self.params
        else :
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
                X, y, test_size=0.3,random_state = 42)
    n_features = X.shape[1]
    params = np.zeros((n_features,1))
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    for val in [0.05,0.1,0.2,1]:
        reg = LassoRegression(alpha=val)
        reg.fit(X_train,y_train)
        print(reg.coef_)
        # print(reg.mean_squared_error())
        print("{} is {}".format(val,reg.score(X_test, y_test)))

class RidgeRegression(LinearRegression):
    def __init__(self,alpha=1):
        self.lamb = alpha
        self.regularization = lambda w : self.lamb * w
        self.lossfunc = lambda w : self.lamb * w.T.dot(w)
        super(RidgeRegression,self).__init__(lamb = self.lamb,reg = self.regularization,lossfunc = self.lossfunc)
    def fit(self,X,y):
        return super(RidgeRegression,self).fit(X,y)
    def predict(self,X,y):
        return super(RidgeRegression,self).predict(X)

class LassoRegression(LinearRegression):
    def __init__(self,alpha=1):
        self.lamb = alpha
        self.lossfunc = lambda w : self.lamb * np.linalg.norm(w)
        self.regularization = lambda w : self.lamb * np.sign(w)
        super(LassoRegression,self).__init__(lamb = self.lamb,reg = self.regularization,lossfunc = self.lossfunc)
    def fit(self,X,y):
        return super(LassoRegression,self).fit(X,y)
    def predict(self,X,y):
        return super(LassoRegression,self).predict(X)



if __name__ == "__main__":
    main()
