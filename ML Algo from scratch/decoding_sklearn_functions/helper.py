import random
import numpy as np
def accuracy_score(y , y_pred):
    if(len(y) != len(y_pred)) : 
        raise Exception('Length mismatch')
    if (type(y)!=type(y_pred)):
        raise Exception('Type mismatch')    
    if(isinstance(y,list)):
        return sum([ 1 for x,y in zip(y , y_pred) if x==y]) / len(y)
    else:
        return (y == y_pred).mean()

def normalize(x,order=2):
    return x / np.linalg.norm(x,order)