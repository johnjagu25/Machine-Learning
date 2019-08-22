from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import math

class KNNClassifier():

    def __init__(self,k_neighbors = 5):
        self.k_neighbors = k_neighbors

    def fit(self,X,y):
        self.X = X
        self.y = y

    def predict(self,X):
        pred_size = X.shape[0]
        y_pred = np.empty(pred_size)
        for i,point1 in enumerate(X):
            cal_dist_index = np.argsort([self.euclidean_distance(point1,point2) for point2 in self.X])
            k_sample = cal_dist_index[:self.k_neighbors]
            k_nearest_neighbors = np.array(self.y[k_sample])
            y_pred[i] = self._majority_vote(k_nearest_neighbors)
        
        return y_pred

    def _majority_vote(self, k_neig_labels):
        #bincount returns the number of occurance of each label at its own index
        counts = np.bincount(k_neig_labels)
        return counts.argmax()

    def score(self,X,y):
        return accuracy_score(self.predict(X),y)
    
    def euclidean_distance(self,p1,p2):
        distance = 0
        data_len = len(p1)
        for i in range(data_len):
            distance += pow((p1[i]-p2[i]),2)
        return math.sqrt(distance)

def main():
    
    dataset = load_iris()
    X = dataset.data
    y = dataset.target 
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
    clf = KNNClassifier(k_neighbors=3)
    clf.fit(X_train,y_train)
    print(clf.score(X_test,y_test))
if __name__ == '__main__':
    main()