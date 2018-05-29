import pandas as pd 
import numpy as np
from numpy import genfromtxt
dataset = genfromtxt('malware+b9after2forWEKA.csv', delimiter=',')
X =dataset[: , 0:1808]
y =dataset[: , 1808:]
np.shape(X)
np.shape(y)
n_samples, n_features = np.shape(X)
print n_samples, n_features
n_labels = np.shape(y)
n_labels
y1 = y.ravel() # 2D array into 1D array
#Split Data into Training and Testing Set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)
print X_train
print X_test
print y_train
print y_test
#Compute fisher score and output the score of each feature:
from skfeature.function.similarity_based import fisher_score
score = fisher_score.fisher_score(X_train, y_train)
print score
idx = fisher_score.feature_ranking(score)
print idx
num_fea = 5 #select no of features
selected_features_train = X_train[:, idx[0:num_fea]]






