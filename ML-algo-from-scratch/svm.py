import numpy as np

class SVMClassifier():
    def __init__(self,C=1,learning_rate = 0.1,n_iter = 10):
        self.C = C
        self.learning_rate = learning_rate;
        self.n_iter = n_iter
        pass
    
    def fit(self,X,y):
        X = np.insert(X, 0, 1, axis=1)
        self.theta = []
        self.n_samples  = X.shape[0]
        labels = np.unique(y)
        for label in labels:
            y_label = np.where(y == label, 1, -1)
            theta = np.ones(X.shape[1])
            for _ in range(self.n_iter):  
                for i, sample in enumerate(X):
                    predictions = np.dot(X[i] , theta)
                    # if signs are not same, it is misclassified
                    if (y_label[i]*predictions < 1):
                        theta +=  self.learning_rate * (self.C * (y_label[i]*sample) - (2*(1/self.n_iter)*theta))
                    else:
                        theta += self.learning_rate * (-2*(1/self.n_iter)*theta)
            self.theta.append((theta, label))
        return self

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        return [self.predict_row(i) for i in X]

    def predict_row(self,X):
        return max((X.dot(coeff), label) for coeff, label in self.theta)[1]


def main():
    from sklearn.datasets import load_digits
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.svm import SVC

    dataset = load_digits()
    X_train,X_test,y_train,y_test = train_test_split(dataset.data,dataset.target,test_size=0.3)

    reg = SVC(gamma='auto')
    reg.fit(X_train,y_train)
    print(accuracy_score(y_test,reg.predict(X_test)))  
    reg1 = SVMClassifier(C = 1,learning_rate = 0.001)
    reg1.fit(X_train,y_train)
    print(accuracy_score(y_test,reg1.predict(X_test)))


if __name__ == "__main__":
    main()
    
