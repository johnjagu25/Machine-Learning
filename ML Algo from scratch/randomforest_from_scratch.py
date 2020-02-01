from decision_tree_from_scratch import DecisionTreeClassifier
from decoding_sklearn_functions.helper import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from scipy import stats
dataset = load_iris()

class RandomForestClassifier1:
    def __init__(self,n_estimators = 2 , max_features = None,n_bootstrap = 50):        
        self.n_estimators = n_estimators
        self.max_features = max_features
        self.n_bootstrap = n_bootstrap
        
    def bootstrapping(self,X):
        bootstrap_indices = np.random.randint(low=0, high=len(X), size=self.n_bootstrap)
        self.X_temp = self.X[bootstrap_indices]
        self.y_temp = self.y[bootstrap_indices]

    def fit(self,X,y):
        self.X = X
        self.y = y
        self.forest = []
        for i in range(self.n_estimators):
            self.bootstrapping(X)
            tree = DecisionTreeClassifier(max_features=self.max_features)
            tree.fit(self.X_temp,self.y_temp)
            self.forest.append(tree)

    def predict(self,y):
        predictions = []
        for val in self.forest:
            predictions.append(val.predict(y))
        return stats.mode(np.array(predictions))[0][0]

score_list = []
X_train,X_test,y_train,y_test = train_test_split(dataset.data,dataset.target,test_size=0.3)
for val in [10,20,50,100]:
    dec = RandomForestClassifier1(n_estimators=val,n_bootstrap = 100,max_features = 2)
    dec.fit(X_train,y_train)
    score_list.append(accuracy_score(y_test,dec.predict(X_test)))
print(score_list)
score_list = []
from sklearn.ensemble import RandomForestClassifier
for val in [10,20,50,100]:
    dec = RandomForestClassifier(n_estimators=val,max_features  = 2)
    dec.fit(X_train,y_train)
    score_list.append(accuracy_score(y_test,dec.predict(X_test)))
print(score_list)
