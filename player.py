"""
Features:
-Round
-Last 5(?) plays (rock/paper/scissors/none)
-Score
-Education
-Age
-Sex
-Income
-Personality type
"""
import pandas as pd
import numpy as np
from naive_bayes import NaiveBayes
from perceptron import  MultiClassPerceptron
number_of_features = 12

#indexes: 0-4 plays, 5 round, 6 score, 7 age, 8 sex, 9 education, 10 income, 11 personality
#zero means not set yet
#plays(num-player,AI): 1-RR 2-RP 3-RS 4-PR 5-PP 6-PS 7-SR 8-SP 9-SS
#round: starting from 0, stops increasing after 9
#score: ranging from 0 to 4, 2 if tie
#age: 0-0to10 1-10to20 2-20to30 3-30to40 ... 9-90 to 100
#sex: 0-male 1-female
#education: 1-none 2-elementary 3-middle 4-high 5-uni 6-master 7-doc

features = np.zeros(number_of_features, dtype = int)
features[6] = 2
#features[7] = (int(input("What is your age? (enter a number) "))/10)+1
features[0] = 0
features[1] = 0
features[2] = 0
features[3] = 0
features[4] = 0
features[5] = 0
num_class = 3
feature_dim = 12
num_value = 10
data = np.load('data.npy')
labels = np.load('labels.npy')
print("Bayes:")
Bayes = NaiveBayes(num_class,feature_dim,num_value)
Bayes.train(data, labels)
guess = Bayes.guess(features)
Bayes.test(data, labels)
print(guess)
print("Perceptron:")
Perceptron = MultiClassPerceptron(num_class,feature_dim)
Perceptron.train(data, labels)
Perceptron.test(data, labels)
