import pandas as pd 
import numpy as np 
from collections import defaultdict
import re
from sklearn.metrics import accuracy_score




def preprocess_string(str_arg): 

    cleaned_str=re.sub('[^a-z\s]+',' ',str_arg,flags=re.IGNORECASE) #every char except alphabets is replaced
    cleaned_str=re.sub('(\s+)',' ',cleaned_str) #multiple spaces are replaced by single space
    cleaned_str=cleaned_str.lower() #converting the cleaned string to lower case
    
    return cleaned_str # eturning the preprocessed string in tokenized form




from sklearn.datasets import fetch_20newsgroups

categories=['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med'] 
newsgroups_train=fetch_20newsgroups(subset='train',categories=categories)


train_data=np.array(newsgroups_train.data) #getting all trainign examples
train_labels=np.array(newsgroups_train.target) #getting training labels
classes = np.unique(train_labels)

probs = {}
probcl = {}
for x in classes:
    mushcl = train_data[train_labels==x]
    clsp = {}
    tot = len(mushcl)
    for col in range(mushcl.shape[1]):
        colp = {}
        for val,cnt in mushcl[col].value_counts().iteritems():
            pr = cnt/tot
            colp[val] = pr
        clsp[col] = colp
    probs[x] = clsp
    probcl[x] = len(mushcl)/len(train_data)

def probabs(x):
    #X - pandas Series with index as feature
    if not isinstance(x,pd.Series):
        raise IOError("Arg must of type Series")
    probab = {}
    for cl in classes:
        pr = probcl[cl]
        for col,val in x.iteritems():
            try:
                pr *= probs[cl][col][val]
            except KeyError:
                pr = 0
        probab[cl] = pr
    return probab


def classify(x):
    probab = probabs(x)
    mx = 0
    mxcl = ''
    for cl,pr in probab.items():
        if pr > mx:
            mx = pr
            mxcl = cl
    return mxcl

b = []
for i in train_data:
    #print(classify(mush.loc[i,features]),mush.loc[i,target])
    b.append(classify(train_data[i]))

print(accuracy_score(train_labels,b))

#Test data
# b = []
# for i in test.index:
#     #print(classify(mush.loc[i,features]),mush.loc[i,target])
#     b.append(classify(test.loc[i,features]) == test.loc[i,target])
# print(sum(b),"correct of",len(test))
# print("Accuracy:",sum(b)/len(test))


# pd.options.display.max_colwidth=250
# pd.DataFrame(data=np.column_stack([train_data,train_labels]),columns=["Training Examples","Training Labels"]).head()


# nb=NaiveBayes(np.unique(train_labels)) #instantiate a NB class object

# print ("---------------- Training In Progress --------------------")
 
# nb.train(train_data,train_labels) #start tarining by calling the train function

# print ('----------------- Training Completed ---------------------')

newsgroups_test=fetch_20newsgroups(subset='test',categories=categories) #loading test data
test_data=newsgroups_test.data #get test set examples
# test_labels=newsgroups_test.target #get test set labels
# print ("Number of Test Examples: ",len(test_data))
# print ("Number of Test Labels: ",len(test_labels))

# pclasses=nb.test(test_data) #get predcitions for test set

# #check how many predcitions actually match original test labels
# test_acc=np.sum(pclasses==test_labels)/float(test_labels.shape[0]) 

# print ("Test Set Examples: ",test_labels.shape[0])
# print ("Test Set Accuracy: ",test_acc*100,"%")
