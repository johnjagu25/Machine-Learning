from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize
import numpy as np
class Adaboost:
    def __init__(self,n_estimators = 100):
        self.n_estimators = n_estimators
        self.tree = []

    def fit(self,X,y):
        estimator_list, alpha_list  = [], []

        n = len(y)
        sample_weight = np.ones(n) / n
        for val in range(self.n_estimators):
            dec = DecisionTreeClassifier(max_depth=1)
            dec.fit(X,y,sample_weight=sample_weight)
            y_predict = dec.predict(X)
            incorrect = (y_predict != y)
            #calculate the total error in the dataset
            error = sum(sample_weight[y != y_predict])
            if error == 0:
                   break
            # calculate alpha
            #when total error is small alpha relatively large andd vice versa
            #when alpha is negative, it votes for inverse value of the prediction
            #below equation fails when error value is 1 or 0, to prevent add a small error
            # estimator_error = np.mean( np.average(incorrect, weights=sample_weight, axis=0))
            alpha = 1/2*np.log((1 - error)/error)
            #misclassified class will get high weight
            sample_weight *= np.exp(alpha * incorrect)
            # normalize
            sample_weight /= np.sum(sample_weight)
            estimator_list.append(dec)
            alpha_list.append(alpha.copy())
        self.estimator_list = np.array(estimator_list)
        self.alpha_list = np.array(alpha_list)
   

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
            weighted_prdicts_i = [(p, alpha) for p , alpha in zip( predicts_i,self.alpha_list)]
            predictions.append(self.weighted_majority_vote(weighted_prdicts_i))

        return predictions
        

def main():
    from sklearn.datasets import load_breast_cancer
    dataset = load_breast_cancer()
    # model= Adaboost(n_estimators = 100)
    X_train,X_test,y_train,y_test = train_test_split(dataset.data,dataset.target,test_size=0.3)
    # model.fit(X_train,y_train)
    # print(accuracy_score(y_test,model.predict(X_test)))
    from sklearn.ensemble import AdaBoostClassifier
    for val in [10,100,200,400,500,1000]:
        model= Adaboost(n_estimators = val)
        model1 = AdaBoostClassifier(n_estimators = val)
        model.fit(X_train,y_train)
        print(accuracy_score(y_test,model.predict(X_test)))
        print("-------scratch-------")
        model1.fit(X_train,y_train)
        print(accuracy_score(y_test,model1.predict(X_test)))
        print("------sklearn--------")


if __name__ == "__main__":
    main()
