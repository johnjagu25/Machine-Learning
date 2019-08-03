#if you have graphviz and not set on the right path then download the file from this path
# https://graphviz.gitlab.io/_pages/Download/Download_windows.html and place those on the below given path
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import math
import random


# we will compare our classifier performance with sklearn classifier

class DecisionTreeClassifier:
    def __init__(self, criterion='gini',max_features = None):
        self.max_features = max_features
        self.criterion = criterion
        self.type = 'numpy'

    def fit(self, X, y,header = None):
        if(type(X) == 'list'):
            self.type = 'list'

        rows = np.column_stack((X, y))

        self.header = header
        self.tree = self.buildTree(rows)
      
        return self.tree

    def buildTree(self, rows):
        
    # Try partitioing the dataset on each of the unique attribute,
    # calculate the information gain,
    # and return the question that produces the highest gain.
        gain, question = self.best_split(rows)

    # Base case: no further info gain
    # Since we can ask no further questions,
    # we'll return a leaf.
        if gain == 0:
            return Leaf(rows)

    # If we reach here, we have found a useful feature / value
    # to partition on.
        true_rows, false_rows = self.partition(rows, question)

    # Recursively build the true branch.
        true_branch = self.buildTree(true_rows)

    # Recursively build the false branch.
        false_branch = self.buildTree(false_rows)

    # Return a Question node.
    # This records the best feature / value to ask at this point,
    # as well as the branches to follow
    # dependingo on the answer.
        return Decision_Node(question, true_branch, false_branch)

    def best_split(self, rows):
        """Find the best question to ask by iterating over every feature / value
        and calculating the information gain."""
        best_gain = 0  # keep track of the best information gain
        best_question = None  # keep train of the feature / value that produced it
        current_uncertainty = self.findImpurity(rows)
        features = len(rows[0]) - 1  # number of columns
        if self.max_features and self.max_features <= features:
            features = random.sample(population=range(features), k=self.max_features)
        for col in features:  # for each feature

            # unique values in the column
            values = set([row[col] for row in rows])

            for val in values:  # for each value

                question = Question(col, val,self.header)

            # try splitting the dataset
                true_rows, false_rows = self.partition(rows, question)

            # Skip this split if it doesn't divide the
            # dataset.
                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue

            # Calculate the information gain from this split
                gain = self.info_gain(
                    true_rows, false_rows, current_uncertainty)

            # You actually can use '>' instead of '>=' here
            # but I wanted the tree to look a certain way for our
            # toy dataset.
                if gain >= best_gain:
                    best_gain, best_question = gain, question

        return best_gain, best_question

    def partition(self, rows, question):
        """Partitions a dataset.
        For each row in the dataset, check if it matches the question. If
        so, add it to 'true rows', otherwise, add it to 'false rows'.
        """
        true_rows, false_rows = [], []
        for row in rows:
            if question.match(row):
                true_rows.append(row)
            else:
                false_rows.append(row)
        return true_rows, false_rows

    def predict(self, row):
        """See the 'rules of recursion' above."""
        predictions = [] 
        for val in row:
            value = self._predict(val,self.tree)
            # predictions.append(self.print_leaf(value))
            predictions.append(value)
        return predictions if self.type == 'list' else np.array(predictions)
    

    def _predict(self, row,node):
        # Base case: we've reached a leaf
        if isinstance(node, Leaf):
            return node.predictions           

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
        if node.question.match(row):
            return self._predict(row, node.true_branch)
        else:
            return self._predict(row, node.false_branch)
            

    
    def unique_val(self, rows, col):
        return set([row[col] for row in rows])    

   

    def findImpurity(self, rows):
        """
        Criterion is used to find the impurity in the dataset.
        We have two used here two criterion, both are pretty much the same.
        I would prefer Gini as it doesn't perform log computation like Entropy
        ref - https://github.com/rasbt/python-machine-learning-book/blob/master/faq/decision-tree-binary.md
        """
        isEntropy = self.criterion == 'entropy'
        counts = class_counts(rows)
        impurity = 0 if isEntropy else 1
    #Gini = 1 - sum(pi**2)
        if isEntropy:
            for lbl in counts:
                prob_of_lbl = counts[lbl] / float(len(rows))
                impurity -= prob_of_lbl * math.log(prob_of_lbl, 2)
        else:
            for lbl in counts:
                prob_of_lbl = counts[lbl] / float(len(rows))
                impurity -= prob_of_lbl**2

        return impurity

    def info_gain(self, left, right, current_uncertainty):
        """Information Gain.

        The uncertainty of the starting node, minus the weighted impurity of
        two child nodes.
        """
        p = float(len(left)) / (len(left) + len(right))
        return current_uncertainty - p * self.findImpurity(left) - (1 - p) * self.findImpurity(right)
    
    def print_tree(self,node, spacing=""):
        """World's most elegant tree printing function."""

        # Base case: we've reached a leaf
        if isinstance(node, Leaf):
            print (spacing + "Predict", node.predictions)
            return

        # Print the question at this node
        print (spacing + str(node.question))

        # Call this function recursively on the true branch
        print (spacing + '--> True:')
        self.print_tree(node.true_branch, spacing + "  ")

        # Call this function recursively on the false branch
        print (spacing + '--> False:')
        self.print_tree(node.false_branch, spacing + "  ")


class Question:
    def __init__(self, column, value,header = None):
        self.column = column
        # value = int(value) if value.isdigit() else value
        self.value = value
        self.header = header

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column] 
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        if self.header is not None:
            # This is just a helper method to print
            # the question in a readable format.
            condition = "=="
            val = self.value 
            if is_numeric(val):
                condition = ">="
            return "Is %s %s %s?" % (
                self.header[self.column], condition, str(val))
        else :
            return ""


class Leaf:
    """A Leaf node classifies data.

    This holds a dictionary of class (e.g., "Apple") -> number of times
    it appears in the rows from the training data that reach this leaf.
    """

    def __init__(self, rows):
        self.predictions = class_counts(rows,True)


class Decision_Node:
    """A Decision Node asks a question.

    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def class_counts(rows, numberRequired=False):
        value = None
        max = 0
        count = {}
        for row in rows:
            label = row[-1]
            if label not in count:
                count[label] = 1
            else:
                count[label] += 1
            if count[label] > max:
                max = count[label]
                value = label
        return value if numberRequired else count

def is_numeric(val):
        return isinstance(val, int) or isinstance(val, float)
# import graphviz
# from sklearn import tree

# #iris dataset
# dataset = load_iris()
# #to load digit dataset comment above line and uncomment the below line
# # dataset = load_digits()
# X_train,X_test,y_train,y_test = train_test_split(dataset.data,dataset.target,test_size=0.3)

# classifiers = [DecisionTreeClassifier(),DecisionTreeClassifier()]

# maxScore = 0
# clIndex = 1


# for i,classifier in enumerate(classifiers):
#     #default criterion is gini. 
#     model = classifier 
#     model.fit(X_train,y_train) 
#     if i==0:
#         value = model.fit(X_train,y_train,header=[ 'sepal length', 'sepal width','petal length', 'petal width'])
#         model.print_tree(value)
#     predictions = model.predict(X_test)
#     plt.figure(figsize = (10,7))
#     sn.heatmap(confusion_matrix(y_test, predictions), annot=True)
#     # plt.show()
#     #if you have graphviz uncomment this line
#     if i == 1:
#         dot_data = tree.export_graphviz(model.fit(X_train,y_train) , out_file=None,  feature_names=[ 'sepal length', 'sepal width','petal length', 'petal width'],  
#             class_names=dataset.target_names,  filled=True, rounded=True, special_characters=True) 
#         graph = graphviz.Source(dot_data)  
#         graph.render('dtree_render',view=True)
        
#     score = accuracy_score(y_test,model.predict(X_test))
#     print(score)
#     if score > maxScore:
#         maxScore = score
#         clIndex = i+1
# print("class {} performs well".format(clIndex))




    

