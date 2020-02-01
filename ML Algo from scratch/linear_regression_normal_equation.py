import numpy as np
import math
from sklearn.datasets import load_boston
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# reference http://www2.lawrence.edu/fast/GREGGJ/Python/numpy/numpyLA.html

class LinearRegressionN():
    def __init__(self):
        pass
    def fit(self, X, y):
        #  formula to find coefficient β = (XT X)-1 XT y
        X = np.insert(X, 0, 1, axis=1)
        Xt = np.transpose(X)
        XtX = np.dot(Xt,X)
        Xty = np.dot(Xt,y)
        inverse = np.linalg.inv(XtX)
        # self.coef_ = np.dot(inverse,Xty)
        # below line is recommended (https://stackoverflow.com/questions/31256252/why-does-numpy-linalg-solve-offer-more-precise-matrix-inversions-than-numpy-li)
        self.coef_ = np.linalg.solve(XtX,Xty)
        

    def predict(self, X):
        # Insert constant ones for bias weights
        X = np.insert(X, 0, 1, axis=1)
        y_pred = X.dot(self.coef_)
        return y_pred
    def score(self,X,y):
        return r2_score(self.predict(X),y)
    
def main():
    dataset = load_boston()
    X = dataset.data
    y = dataset.target
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
    reg = LinearRegression()
    reg.fit(X_train,y_train)
    print(reg.coef_)
    print(reg.score(X_test,y_test))
 
    

if __name__ == "__main__":
    main()