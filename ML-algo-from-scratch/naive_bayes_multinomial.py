from sklearn.datasets import fetch_20newsgroups 
from collections import defaultdict
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
import re
import numpy as np


def preprocessing_string(documents):
        processed_data = []
        for index,data in enumerate(documents):
            # keeping only alphabets
            processed_str=re.sub('[^a-z\s]+',' ',data.lower(),flags=re.IGNORECASE)
            # multiple spaces are replace by single space
            processed_str=re.sub('(\s+)',' ',processed_str)
            processed_data.append(processed_str)        
        return np.array(processed_data)


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
        self.bow_dict = []
        self.vocab_size = None

    def fit(self,X,y):
        self.classes = np.unique(y)
        self.n_classes = self.classes.shape[0]
        self.X = X
        self.y = np.array(y)        
        self.class_word_count = np.empty(self.n_classes)
        vocab_words = []
        for index,cls_label in enumerate(self.classes):
            self.bow_dict.append(defaultdict(lambda :0))
            self._addToBow(index,cls_label)
            self.class_word_count[index] = np.sum(list(self.bow_dict[index].values()))
            vocab_words += self.bow_dict[index].keys()
        vocab_unique = np.unique(vocab_words) 
        self.vocab_size = vocab_unique.shape[0]

    def predict(self,X):
        predictions = []
        for test in X:                           
            post_prob=self._predict_row(test) 
            predictions.append(self.classes[np.argmax(post_prob)])
        return np.array(predictions) 

    def _predict_row(self,x):
        posterior_prob = np.empty(self.n_classes)
        for index,cls_label in enumerate(self.classes):
            likelihood_prob = self._cal_likelihood(x,index)
            prior_prob = self._cal_prior(cls_label)
            posterior_prob[index]=likelihood_prob + np.log(prior_prob)                                 
        return posterior_prob

    def _addToBow(self,index,cls_label):
        filter_cls_label = self.X[self.y == cls_label] 
        for list_words in filter_cls_label :
            for word in list_words.split():
                self.bow_dict[index][word] += 1

    def _cal_prior(self,cls_label):
        return (self.y == cls_label).mean()

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
    newsgroups_train=fetch_20newsgroups(subset='train',categories=categories,shuffle=True)
    newsgroups_test=fetch_20newsgroups(subset='test',categories=categories,shuffle=True)
    X_train = preprocessing_string(np.array(newsgroups_train.data))
    y_train = newsgroups_train.target
    X_test  = preprocessing_string(np.array(newsgroups_test.data))
    y_test  = newsgroups_test.target

    #Python scratch implementation
    Nb = NaiveBayes()    
    Nb.fit(X_train,y_train)  
    print(accuracy_score(y_test,Nb.predict(X_test)))

    # Sklearn implementation
    count_vect = CountVectorizer() 
    X_train_count_vect = count_vect.fit_transform(X_train) 
    y_train = newsgroups_train.target

    Nb = MultinomialNB()
    Nb.fit(X_train_count_vect,y_train)
    X_test_counts = count_vect.transform(X_test) 
    y_test = newsgroups_test.target
    print(accuracy_score(y_test,Nb.predict(X_test_counts)))

    # piepline implementation
    # CountVectorizer does the preprocessing by converting text into lowercase and removing 
    # punctuation. So input to it must be a text document
    Nb=Pipeline([('vect', CountVectorizer()),('clf', MultinomialNB())])
    Nb.fit(X_train,y_train)
    print(accuracy_score(y_test,Nb.predict(X_test)))
      






if __name__ == "__main__":
    main()



