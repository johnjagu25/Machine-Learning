import numpy as np
import math

class NaiveBayes():
    """
    Baye's theorem : 
    posterior = (prior * likelihood) / marginal probablity
    p(y|X) = (p(y) * p(X|y)) / p(X)
    Ignore the marginal probablity denominator since this is same for all class.

    Naive baye's assumption :
    Features are conditionally independent from one another
    p(y|(X1,X2,X3)) =  (p(y) * p(X1|y) *  p(X2|y) *  p(X3|y)) / (p(X1) * p(X2) * p(X3))

    Gaussian Likelihood for p(X1|y) :
    coefficient = ( 1/sqrt(2*pi*var of X1 in given y) ) 
    exponent = exp -((new data of X1 - mean of X1 in given y)**2/2*var of X1 in given y)    
    p(X1|y) = coefficient * exponent
    
     """

    def fit(self, X, y):
        self.X, self.y = X, y
        self.classes = np.unique(y)
        self.arguments = []
        self.columns = self.X.shape[1]
        # calculating mean and feature of each features of each class
        for label in self.classes:
            fil_feature = self.X[y == label]
            self.arguments.append([])
            for col in range(self.columns) :
                mean = fil_feature[:,col].mean()
                var = fil_feature[:,col].var()
                self.arguments[label].append({'mean':mean,'variance':var})        

    def _cal_prior(self,label):
        return (self.y == label).mean()

    def _cal_likelihood(self,X,mean,variance):
        # adding small_error to avoid dividing by zero error
        small_error = 1e-7
        exponent =  np.exp(-((X-mean)**2)/(2  * variance + small_error))
        p_likelihood = 1/math.sqrt(2 * math.pi * variance + small_error) * exponent
        return p_likelihood

    def _predict_row(self,X):
        posterior_list = []
        for label in self.classes:
            likelihood_total = 1
            for col in range(self.columns):
                mean = self.arguments[label][col]['mean']
                variance = self.arguments[label][col]['variance']
                likelihood_total *= self._cal_likelihood(X[col],mean,variance)
            posterior = likelihood_total * self._cal_prior(label)
            posterior_list.append(posterior)
        return self.classes[np.argmax(posterior_list)]

    def predict(self, X):
        """ Predict the class labels of the samples in X """
        y_pred = [self._predict_row(sample) for sample in X]
        return y_pred

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
dataset = load_iris()
X_train,X_test,y_train,y_test = train_test_split(dataset.data,dataset.target,test_size=0.3,random_state=42)
reg = NaiveBayes()
reg.fit(X_train,y_train)
print(accuracy_score(reg.predict(X_test),y_test))