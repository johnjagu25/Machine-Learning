import numpy as np
from sklearn.datasets import fetch_20newsgroups 
import re
from collections import defaultdict
from sklearn.metrics import accuracy_score


class NaiveBayes():
    """
    Naive assumption:
    The effect of the occurrence of any of the events is completely independent of the occurrence 
    of other events.

    posterior = (prior * likelihood) / marginal probablity
    p(y|X) = (p(y) * p(X|y)) / p(X)
    Ignore the marginal probablity denominator since this is same for all class.

    likelihood:
    p(X|y) = p(X1|y) * p(X2|y) * p(Xn|y) * p(y)
    p(X1|y) = (count of tokenised words in class + 1) / (total counts of words in class + vocabulary + 1)
    """
    def __init__(self):
        pass


    def fit(self,X,y):
        self.labels = np.unique(y)
        self.n_samples = y.shape[0]
        self.n_classes = self.labels.shape[0]
        self.X = self._preprocessing_string(np.array(X))
        self.y = np.array(y)
        self.bow_dict = []
        self.class_word_count = np.empty(self.n_classes)
        vocab_words = []
        for index,label in enumerate(self.labels):
            self.bow_dict.append(defaultdict(lambda :0))
            self._addToBow(index,label)
            self.class_word_count[index] = np.sum(list(self.bow_dict[index].values()))
            vocab_words += self.bow_dict[index].keys()
        vocab_unique = np.unique(vocab_words) 
        self.vocab_size = vocab_unique.shape[0]

    def predict(self,X):
        X = self._preprocessing_string(X)
        predictions = []
        for test in X:                           
            post_prob=self._predict_row(test) 
            predictions.append(self.labels[np.argmax(post_prob)])
        return np.array(predictions) 

    def _predict_row(self,x):
        posterior_prob = np.empty(self.n_classes)
        for index,label in enumerate(self.labels):
            likelihood_prob = self._cal_likelihood(x,index)
            prior_prob = self._cal_prior(label)
            posterior_prob[index]=likelihood_prob + np.log(prior_prob)                                 
        return posterior_prob

    def _addToBow(self,index,label):
        filter_label = self.X[self.y == label] 
        for list_words in filter_label :
            for word in list_words.split():
                self.bow_dict[index][word] += 1

    def _cal_prior(self,label):
        return (self.y == label).mean()
    
    def _preprocessing_string(self,datas):
        processed_data = []
        for index,data in enumerate(datas):
            cleaned_str=re.sub('[^a-z\s]+',' ',data.lower(),flags=re.IGNORECASE)
            cleaned_str=re.sub('(\s+)',' ',cleaned_str)
            processed_data.append(cleaned_str)        
        return np.array(processed_data)

    def _cal_likelihood(self,x,index):
        # laplace correction adding 1 to avoid zero probablity
        likelihood = 0
        for word in x.split():
            word_counts=self.bow_dict[index][word]+1
            denom = float(self.class_word_count[index]+self.vocab_size+1)
            word_count_prob = word_counts / denom
            likelihood += np.log(word_count_prob)
        return likelihood


def main():
    categories=['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med'] 
    newsgroups_train=fetch_20newsgroups(subset='train',categories=categories)
    X_train , y_train = newsgroups_train.data,newsgroups_train.target
    reg = NaiveBayes()
    reg.fit(X_train,y_train)

    newsgroups_test=fetch_20newsgroups(subset='test',categories=categories)
    X_test=newsgroups_test.data 
    y_test=newsgroups_test.target
    print(accuracy_score(y_test,reg.predict(X_test)))


if __name__ == "__main__":
    main()



