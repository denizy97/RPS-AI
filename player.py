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
from q_learning import Q_Agent
number_of_features_bayes = 12
number_of_features_NN = 32
"""
FOR NAIVE BAYES:
#indexes: 0-4 plays, 5 round, 6 score, 7 age, 8 sex, 9 education, 10 income, 11 personality
#zero means not set yet
#plays(in format player,AI): 1-RR 2-RP 3-RS 4-PR 5-PP 6-PS 7-SR 8-SP 9-SS
#round: starting from 0, stops increasing after 9
#score: ranging from 0 to 4, 2 if tie
#age: 0-0to10 1-10to20 2-20to30 3-30to40 ... 9-90 to 100
#sex: 0-male 1-female
#education: 1-none 2-elementary 3-middle 4-high 5-uni 6-master 7-doc
"""
bayes_features = np.zeros(number_of_features_bayes, dtype = int)
bayes_features[6] = 2
#bayes_features[7] = (int(input("What is your age? (enter a number) "))/10)+1
bayes_features[0] = 0
bayes_features[1] = 0
bayes_features[2] = 0
bayes_features[3] = 0
bayes_features[4] = 0
bayes_features[5] = 0
"""
FEATURE INDEXES FOR NEURAL NETS:
[0]: did I play R last round? (0/1)
[1]: did I play P last round? (0/1)
[2]: did I play S last round? (0/1)
[3,4,5]: did enemy play R/P/S last round? (0/1)
[6,7,8]: did I play R/P/S 2 rounds ago? (0/1)
[9,10,11] did enemy play R/P/S 2 rounds ago? (0/1)
[12,13,14]: did I play R/P/S 3 rounds ago? (0/1)
[15,16,17]: did enemy play R/P/S 3 rounds ago? (0/1)
[18-23]: did I & enemy play R/P/S 4 rounds aho? (0/1)
[24-29]: did I & enemy play R/P/S 5 rounds aho? (0/1)
[30]: round (1-10)/10
[31]: score (-1/-0.5/0/0.5/1)
--- end of game data, start of personal data ---
[32]: age (value/100)
[33]: male/???/female (1/0/-1)
[34]: education (?)
[35]: income (?)
"""
num_class = 3
feature_dim = 12
num_value = 10
data = np.load('data.npy')
labels = np.load('labels.npy')
print("Bayes:")
Bayes = NaiveBayes(num_class,feature_dim,num_value)
Bayes.train(data, labels)
guess = Bayes.guess(bayes_features)
Bayes.test(data, labels)
print(guess)
print("Perceptron:")
Perceptron = MultiClassPerceptron(num_class,feature_dim)
Perceptron.train(data, labels)
Perceptron.test(data, labels)
print("Q Agent:")
Reinforcement = Q_Agent(("rock", "paper", "scissors"), 5, 40, 0.7)
Reinforcement.train(data, labels)
