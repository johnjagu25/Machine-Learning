from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize
import numpy as np
class Adaboost:
    def __init__(self,n_estimators = 100,n_samples=None):
        self.n_samples = n_samples;
        self.n_estimators = n_estimators
        self.tree = []

    def fit(self,X,y):
        
        estimator_list, estimator_weight_list  = [], []

        n = len(y)
        sample_weight = np.ones(n) / n
        
        for val in range(self.n_estimators):
            indices = [i for i in np.random.choice(X.shape[0], X.shape[0], p=sample_weight)]
            X = X[indices]
            y = y[indices]
            dec = DecisionTreeClassifier(max_depth=1)
            dec.fit(X,y)
            y_predict = dec.predict(X)
            incorrect = (y_predict != y)
            estimator_error = np.mean( np.average(incorrect, weights=sample_weight, axis=0))
            estimator_weight = 1/2*np.log((1 - estimator_error)/estimator_error)

            sample_weight *= np.exp(estimator_weight * incorrect * ((sample_weight > 0) | (estimator_weight < 0)))
            if np.isnan(np.sum(sample_weight)):
                sample_weight *= np.exp(estimator_weight * incorrect * ((sample_weight > 0) | (estimator_weight < 0)))
            sample_weight_sum = np.sum(sample_weight)
            # normalize
            sample_weight /= sample_weight_sum
            estimator_list.append(dec)
            estimator_weight_list.append(estimator_weight.copy())
        self.estimator_list = np.array(estimator_list)
        self.estimator_weight_list = np.array(estimator_weight_list)
   

    def weighted_majority_vote(self, weighted_prediction):
        weighted_vote = {}
        for label, weight in weighted_prediction:
            if label in weighted_vote:
                weighted_vote[label] += weight
            else:
                weighted_vote[label] = weight

        max_weight = 0
        max_vote = 0
        for vote, weight in weighted_vote.items():
            if max_weight < weight:
                max_weight = weight
                max_vote = vote

        return max_vote
   
    def predict(self, X):        
        predictions = []
        for i in range(X.shape[0]):
            predicts_i = np.array([estimator.predict([X[i]])[0] for estimator in self.estimator_list])
            weighted_prdicts_i = [(p, alpha) for p , alpha in zip( predicts_i,self.estimator_weight_list)]
            predictions.append(self.weighted_majority_vote(weighted_prdicts_i))
        return predictions
        

def main():
    from sklearn.datasets import load_breast_cancer
    dataset = load_breast_cancer()
    
    X_train,X_test,y_train,y_test = train_test_split(dataset.data,dataset.target,test_size=0.3)
    for val in [10,100,200,400,500,1000]:
        model= Adaboost(n_samples=400,n_estimators = val)
        model.fit(X_train,y_train)
        print(accuracy_score(y_test,model.predict(X_test)))
        print("--------------")


if __name__ == "__main__":
    main()