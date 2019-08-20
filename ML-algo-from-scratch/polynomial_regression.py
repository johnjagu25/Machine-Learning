from itertools import combinations_with_replacement
import numpy as np
# from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
from linear_regression_gradient_descent import LinearRegression



class PolynomialRegression():
    def __init__(self,learning_rate,n_iter,precision=None,degree = 2):
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.precision = precision
        self.degree = degree
    def polynomial_feature(self,x):
        n_samples,n_features = x.shape
        combination = [combinations_with_replacement(range(n_features), i) for i in range(0, self.degree + 1)]
        conv_comb_list =  [item for subcomb in combination for item in subcomb]
        n_output_features = len(conv_comb_list)
        X_new = np.empty((n_samples, n_output_features))    
        for i, index_combs in enumerate(conv_comb_list):  
            X_new[:, i] = np.prod(x[:, index_combs], axis=1)
        return X_new

    def fit(self,X,y):
        X = (X - np.mean(X,0)) / np.std(X,0)
        self.X = self.polynomial_feature(X)
        self.y = y
        self.reg = LinearRegression(polyReg = True)
        self.reg.fit(self.X,self.y)
    def predict(self,X):
        X = (X - np.mean(X,0)) / np.std(X,0)
        X = self.polynomial_feature(X)
        return self.reg.predict(X)

def main():

    from sklearn.datasets import load_boston
    from sklearn.metrics import r2_score
    dataset = load_boston()
    dataset.data = dataset.data[:,[5]]
    X_train,X_test,y_train,y_test = train_test_split(dataset.data,dataset.target,test_size=0.3)
    reg =  PolynomialRegression(learning_rate = 0.5,n_iter = 1000,precision = True,degree=4)
    reg.fit(X_train,y_train)
    print(r2_score(y_train,reg.predict(X_train)))
    print(r2_score(y_test,reg.predict(X_test)))


if __name__ == "__main__":
    main()