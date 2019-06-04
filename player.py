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
number_of_features = 12

#indexes: 0-4 plays, 5 round, 6 score, 7 age, 8 sex, 9 education, 10 income, 11 personality
#zero means not set yet
#plays(num-player,AI): 1-RR 2-RP 3-RS 4-PR 5-PP 6-PS 7-SR 8-SP 9-SS
#round: starting from 1, stops increasing after 10
#score: ranging from -2 to 2, 0 if tie
#age: 1-0to10 2-10to20 3-20to30 4-30to40 ... 10-90 to 100
#sex: 1-male -1-female
#education: 1-none 2-elementary 3-middle 4-high 5-uni 6-master 7-doc

features = np.zeros(number_of_features)
features[5] += 1
features[6] = (int(input("What is your age? (enter a number) "))/10)+1
client = input('(ROUND 1) r/p/s: ')
