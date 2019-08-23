import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class LogisiticRegressions():

    """ Logistic Regression is a classification algorithm.
        Implementation is almost similar to Linear Regression. There is a small change in hypothesis.
        I would recommend you to compare both the implementation.
        Our algorithm uses One vs All strategy.  
        One-vs-all classification is a method which involves training N distinct binary classifiers,
        each designed for recognizing a particular class
          """

    def __init__(self, alpha=0.1, n_iter=1000):
        self.alpha = alpha
        self.n_iter = n_iter

    def fit(self, X, y):
        X = np.insert(X, 0, 1, axis=1)
        self.theta = []
        self.n_samples  = X.shape[0]
        labels = np.unique(y)
        for label in labels:
            y_label = np.where(y == label, 1, 0)
            theta = np.ones(X.shape[1])
            for _ in range(self.n_iter):
                predictions = self.sigmoid(X.dot(theta))
                errors = y_label - predictions
                theta -= -(self.alpha / self.n_samples )* X.T @ errors
            self.theta.append((theta, label))
        return self

    def score(self, X, y):
        return sum(self.predict(X) == y) / len(y)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        return [self.predict_row(i) for i in X]

    def predict_row(self,X):
        return max((X.dot(coeff), label) for coeff, label in self.theta)[1]

   
def main():
    dataset = load_iris()
    X_train,X_test,y_train,y_test = train_test_split(dataset.data,dataset.target,test_size=0.3)
    reg = LogisiticRegressions()
    reg.fit(X_train,y_train)
    print(reg.score(X_test,y_test))
    reg1 = LogisticRegression(solver='lbfgs',multi_class ='ovr')
    reg1.fit(X_train,y_train)
    print(reg1.score(X_test,y_test))


if __name__ == "__main__":
    main()
