from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import math

class KNNClassifier():

    def __init__(self,n_neighbors = 5):
        self.n_neighbors = n_neighbors
        self.k_neighbors_values = []
        self.nearest_distance_points = []
        self.nearest_points_index = []

    def fit(self,X,y):
        self.X = X
        self.y = y

    def predict(self,X):
        pred_size = X.shape[0]
        y_pred = np.empty(pred_size)
        for i,point1 in enumerate(X):
            # calculating distance between the train and test coordinate
            dist = [self._euclidean_distance(point1,point2) for point2 in self.X]
            # sorting the value and taking the index of it
            cal_min_dist_index = np.argsort(dist)
            self.nearest_distance_points.append(np.array(dist)[cal_min_dist_index])
            # nearest value to the y point
            k_sample = cal_min_dist_index[:self.n_neighbors]
            k_nearest_neighbors = np.array(self.y[k_sample])
            self.nearest_points_index.append(cal_min_dist_index)   
            y_pred[i] = self._mode(k_nearest_neighbors)

        return y_pred

    def kneighbors(self,X,n_neighbors = None,return_distance=True):
        if n_neighbors is not None:
            self.n_neighbors = n_neighbors
        self.predict(X)
        if return_distance:
            self.k_neighbors_values.append(self.nearest_distance_points)
        self.k_neighbors_values.append(self.nearest_points_index)
        return self.k_neighbors_values
    
    
    def score(self,X,y):
        return accuracy_score(self.predict(X),y)
    
    def _euclidean_distance(self,p1,p2):
        distance = 0
        data_len = len(p1)
        for i in range(data_len):
            distance += pow((p1[i]-p2[i]),2)
        return math.sqrt(distance)
    
    def _mode(self, k_neig_labels):
        # Label with highest occurence will be selected
        #bincount returns the number of occurance of each label at its own index
        counts = np.bincount(k_neig_labels)
        return counts.argmax()    


def main():    
    dataset = load_iris()
    X = dataset.data
    y = dataset.target 
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
    clf = KNNClassifier(n_neighbors=3)
    clf.fit(X_train,y_train)
    print(clf.score(X_test,y_test))
    clf2 = KNNClassifier(n_neighbors=3)
    clf2.fit(X_train,y_train)
    print(clf2.score(X_test,y_test))
if __name__ == '__main__':
    main()