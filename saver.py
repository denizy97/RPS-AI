import pandas as pd
import numpy as np
#data = pd.read_excel("data.xlsx")
#print(data)
#np.save('data.npy', data)
#array_reloaded = np.load('data.npy')
#print(array_reloaded)
#print(array_reloaded[1][3])
"""Constants"""
NUM_CLASSES = int(3060)
NUM_FEATURES_BAYES = int(12)
NUM_FEATURES_NN = int(32)
"""---"""

def NN_feature_shift(feature_list, rock_list, paper_list, scissors_list, e_rock_list, e_paper_list, e_scissors_list, index):
    feature_list[index][24] = feature_list[index-1][18]
    feature_list[index][18] = feature_list[index-1][12]
    feature_list[index][12] = feature_list[index-1][6]
    feature_list[index][6] = feature_list[index-1][0]
    feature_list[index][0] = rock_list[index-1]
    feature_list[int(index+(NUM_CLASSES/2))][24] = feature_list[int(index+(NUM_CLASSES/2))-1][18]
    feature_list[int(index+(NUM_CLASSES/2))][18] = feature_list[int(index+(NUM_CLASSES/2))-1][12]
    feature_list[int(index+(NUM_CLASSES/2))][12] = feature_list[int(index+(NUM_CLASSES/2))-1][6]
    feature_list[int(index+(NUM_CLASSES/2))][6] = feature_list[int(index+(NUM_CLASSES/2))-1][0]
    feature_list[int(index+(NUM_CLASSES/2))][0] = rock_list[int(index+(NUM_CLASSES/2))-1]

    feature_list[index][25] = feature_list[index-1][19]
    feature_list[index][19] = feature_list[index-1][13]
    feature_list[index][13] = feature_list[index-1][7]
    feature_list[index][7] = feature_list[index-1][1]
    feature_list[index][1] = paper_list[index-1]
    feature_list[int(index+(NUM_CLASSES/2))][25] = feature_list[int(index+(NUM_CLASSES/2))-1][19]
    feature_list[int(index+(NUM_CLASSES/2))][19] = feature_list[int(index+(NUM_CLASSES/2))-1][13]
    feature_list[int(index+(NUM_CLASSES/2))][13] = feature_list[int(index+(NUM_CLASSES/2))-1][7]
    feature_list[int(index+(NUM_CLASSES/2))][7] = feature_list[int(index+(NUM_CLASSES/2))-1][1]
    feature_list[int(index+(NUM_CLASSES/2))][1] = paper_list[int(index+(NUM_CLASSES/2))-1]

    feature_list[index][26] = feature_list[index-1][20]
    feature_list[index][20] = feature_list[index-1][14]
    feature_list[index][14] = feature_list[index-1][8]
    feature_list[index][8] = feature_list[index-1][2]
    feature_list[index][2] = scissors_list[index-1]
    feature_list[int(index+(NUM_CLASSES/2))][26] = feature_list[int(index+(NUM_CLASSES/2))-1][20]
    feature_list[int(index+(NUM_CLASSES/2))][20] = feature_list[int(index+(NUM_CLASSES/2))-1][14]
    feature_list[int(index+(NUM_CLASSES/2))][14] = feature_list[int(index+(NUM_CLASSES/2))-1][8]
    feature_list[int(index+(NUM_CLASSES/2))][8] = feature_list[int(index+(NUM_CLASSES/2))-1][2]
    feature_list[int(index+(NUM_CLASSES/2))][2] = scissors_list[int(index+(NUM_CLASSES/2))-1]

    feature_list[index][27] = feature_list[index-1][21]
    feature_list[index][21] = feature_list[index-1][15]
    feature_list[index][15] = feature_list[index-1][9]
    feature_list[index][9] = feature_list[index-1][3]
    feature_list[index][3] = e_rock_list[index-1]
    feature_list[int(index+(NUM_CLASSES/2))][27] = feature_list[int(index+(NUM_CLASSES/2))-1][21]
    feature_list[int(index+(NUM_CLASSES/2))][21] = feature_list[int(index+(NUM_CLASSES/2))-1][15]
    feature_list[int(index+(NUM_CLASSES/2))][15] = feature_list[int(index+(NUM_CLASSES/2))-1][9]
    feature_list[int(index+(NUM_CLASSES/2))][9] = feature_list[int(index+(NUM_CLASSES/2))-1][3]
    feature_list[int(index+(NUM_CLASSES/2))][3] = e_rock_list[int(index+(NUM_CLASSES/2))-1]

    feature_list[index][28] = feature_list[index-1][22]
    feature_list[index][22] = feature_list[index-1][16]
    feature_list[index][16] = feature_list[index-1][10]
    feature_list[index][10] = feature_list[index-1][4]
    feature_list[index][4] = e_paper_list[index-1]
    feature_list[int(index+(NUM_CLASSES/2))][28] = feature_list[int(index+(NUM_CLASSES/2))-1][22]
    feature_list[int(index+(NUM_CLASSES/2))][22] = feature_list[int(index+(NUM_CLASSES/2))-1][16]
    feature_list[int(index+(NUM_CLASSES/2))][16] = feature_list[int(index+(NUM_CLASSES/2))-1][10]
    feature_list[int(index+(NUM_CLASSES/2))][10] = feature_list[int(index+(NUM_CLASSES/2))-1][4]
    feature_list[int(index+(NUM_CLASSES/2))][4] = e_paper_list[int(index+(NUM_CLASSES/2))-1]

    feature_list[index][29] = feature_list[index-1][23]
    feature_list[index][23] = feature_list[index-1][17]
    feature_list[index][17] = feature_list[index-1][11]
    feature_list[index][11] = feature_list[index-1][5]
    feature_list[index][5] = e_scissors_list[index-1]
    feature_list[int(index+(NUM_CLASSES/2))][29] = feature_list[int(index+(NUM_CLASSES/2))-1][23]
    feature_list[int(index+(NUM_CLASSES/2))][23] = feature_list[int(index+(NUM_CLASSES/2))-1][17]
    feature_list[int(index+(NUM_CLASSES/2))][17] = feature_list[int(index+(NUM_CLASSES/2))-1][11]
    feature_list[int(index+(NUM_CLASSES/2))][11] = feature_list[int(index+(NUM_CLASSES/2))-1][5]
    feature_list[int(index+(NUM_CLASSES/2))][5] = e_scissors_list[int(index+(NUM_CLASSES/2))-1]

    return


"""
list[class, feature]: list of features for each class
labels[class]: ENEMY label for each class (rock, paper or scissors)
plays[class]: the play by both players in each class (rock-rock, rock-paper, ..., scissors-scissors)
"""
list = np.zeros((NUM_CLASSES, NUM_FEATURES_BAYES), dtype = int)
nn_list = np.zeros((NUM_CLASSES, NUM_FEATURES_NN))
labels = np.zeros((NUM_CLASSES), dtype = int)
plays = np.zeros((NUM_CLASSES), dtype = int)
rocks = np.zeros((NUM_CLASSES), dtype = int)
papers = np.zeros((NUM_CLASSES), dtype = int)
scissors = np.zeros((NUM_CLASSES), dtype = int)
e_rocks = np.zeros((NUM_CLASSES), dtype = int)
e_papers = np.zeros((NUM_CLASSES), dtype = int)
e_scissors = np.zeros((NUM_CLASSES), dtype = int)
list[:, 6] = 2 #score starts at 2 so initialize that feature to 2 for all
f = open("data.txt", "r")
index = 0 #class idx
round = 0 #round of current game (game is best of 3), max value is 9
unique = True #is it the first play in a game of best of 3
for line in f:
    if "ss" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[int(index+(NUM_CLASSES/2))][4] = list[int(index+(NUM_CLASSES/2))-1][3]
            list[int(index+(NUM_CLASSES/2))][3] = list[int(index+(NUM_CLASSES/2))-1][2]
            list[int(index+(NUM_CLASSES/2))][2] = list[int(index+(NUM_CLASSES/2))-1][1]
            list[int(index+(NUM_CLASSES/2))][1] = list[int(index+(NUM_CLASSES/2))-1][0]
            list[int(index+(NUM_CLASSES/2))][0] = plays[int(index+(NUM_CLASSES/2))-1]
            NN_feature_shift(nn_list, rocks, papers, scissors, e_rocks, e_papers, e_scissors, index)
        plays[index] = 1
        plays[int(index+(NUM_CLASSES/2))] = 1
        rocks[index] = 1
        rocks[int(index+(NUM_CLASSES/2))] = 1
        e_rocks[index] = 1
        e_rocks[int(index+(NUM_CLASSES/2))] = 1
        labels[index] = 0
        labels[int(index+(NUM_CLASSES/2))] = 0
        list[index][5] = round
        list[int(index+(NUM_CLASSES/2))][5] = round
        nn_list[index][30] = (round+1)/10
        nn_list[int(index+(NUM_CLASSES/2))][30] = (round+1)/10
        if index != NUM_CLASSES-1 and index != (NUM_CLASSES/2)-1:
            list[index+1][6] += 0
            list[int(index+(NUM_CLASSES/2))+1][6] += 0
            nn_list[index+1][6] += 0
            nn_list[int(index+(NUM_CLASSES/2))+1][6] += 0
    elif "sp" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[int(index+(NUM_CLASSES/2))][4] = list[int(index+(NUM_CLASSES/2))-1][3]
            list[int(index+(NUM_CLASSES/2))][3] = list[int(index+(NUM_CLASSES/2))-1][2]
            list[int(index+(NUM_CLASSES/2))][2] = list[int(index+(NUM_CLASSES/2))-1][1]
            list[int(index+(NUM_CLASSES/2))][1] = list[int(index+(NUM_CLASSES/2))-1][0]
            list[int(index+(NUM_CLASSES/2))][0] = plays[int(index+(NUM_CLASSES/2))-1]
            NN_feature_shift(nn_list, rocks, papers, scissors, e_rocks, e_papers, e_scissors, index)
        plays[index] = 2
        plays[int(index+(NUM_CLASSES/2))] = 4
        rocks[index] = 1
        papers[int(index+(NUM_CLASSES/2))] = 1
        e_papers[index] = 1
        e_rocks[int(index+(NUM_CLASSES/2))] = 1
        labels[index] = 0
        labels[int(index+(NUM_CLASSES/2))] = 1
        list[index][5] = round
        list[int(index+(NUM_CLASSES/2))][5] = round
        nn_list[index][30] = (round+1)/10
        nn_list[int(index+(NUM_CLASSES/2))][30] = (round+1)/10
        if index != NUM_CLASSES-1 and index != (NUM_CLASSES/2)-1:
            list[index+1][6] += -1
            list[int(index+(NUM_CLASSES/2))+1][6] += 1
            nn_list[index+1][6] += -0.5
            nn_list[int(index+(NUM_CLASSES/2))+1][6] += 0.5
    elif "sx" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[int(index+(NUM_CLASSES/2))][4] = list[int(index+(NUM_CLASSES/2))-1][3]
            list[int(index+(NUM_CLASSES/2))][3] = list[int(index+(NUM_CLASSES/2))-1][2]
            list[int(index+(NUM_CLASSES/2))][2] = list[int(index+(NUM_CLASSES/2))-1][1]
            list[int(index+(NUM_CLASSES/2))][1] = list[int(index+(NUM_CLASSES/2))-1][0]
            list[int(index+(NUM_CLASSES/2))][0] = plays[int(index+(NUM_CLASSES/2))-1]
            NN_feature_shift(nn_list, rocks, papers, scissors, e_rocks, e_papers, e_scissors, index)
        plays[index] = 3
        plays[int(index+(NUM_CLASSES/2))] = 7
        rocks[index] = 1
        scissors[int(index+(NUM_CLASSES/2))] = 1
        e_scissors[index] = 1
        e_rocks[int(index+(NUM_CLASSES/2))] = 1
        labels[index] = 0
        labels[int(index+(NUM_CLASSES/2))] = 2
        list[index][5] = round
        list[int(index+(NUM_CLASSES/2))][5] = round
        nn_list[index][30] = (round+1)/10
        nn_list[int(index+(NUM_CLASSES/2))][30] = (round+1)/10
        if index != NUM_CLASSES-1 and index != (NUM_CLASSES/2)-1:
            list[index+1][6] += 1
            list[int(index+(NUM_CLASSES/2))+1][6] += -1
            nn_list[index+1][6] += 0.5
            nn_list[int(index+(NUM_CLASSES/2))+1][6] += -0.5
    elif "ps" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[int(index+(NUM_CLASSES/2))][4] = list[int(index+(NUM_CLASSES/2))-1][3]
            list[int(index+(NUM_CLASSES/2))][3] = list[int(index+(NUM_CLASSES/2))-1][2]
            list[int(index+(NUM_CLASSES/2))][2] = list[int(index+(NUM_CLASSES/2))-1][1]
            list[int(index+(NUM_CLASSES/2))][1] = list[int(index+(NUM_CLASSES/2))-1][0]
            list[int(index+(NUM_CLASSES/2))][0] = plays[int(index+(NUM_CLASSES/2))-1]
            NN_feature_shift(nn_list, rocks, papers, scissors, e_rocks, e_papers, e_scissors, index)
        plays[index] = 4
        plays[int(index+(NUM_CLASSES/2))] = 2
        papers[index] = 1
        rocks[int(index+(NUM_CLASSES/2))] = 1
        e_rocks[index] = 1
        e_papers[int(index+(NUM_CLASSES/2))] = 1
        labels[index] = 1
        labels[int(index+(NUM_CLASSES/2))] = 0
        list[index][5] = round
        list[int(index+(NUM_CLASSES/2))][5] = round
        nn_list[index][30] = (round+1)/10
        nn_list[int(index+(NUM_CLASSES/2))][30] = (round+1)/10
        if index != NUM_CLASSES-1 and index != (NUM_CLASSES/2)-1:
            list[index+1][6] += 1
            list[int(index+(NUM_CLASSES/2))+1][6] += -1
            nn_list[index+1][6] += 0.5
            nn_list[int(index+(NUM_CLASSES/2))+1][6] += -0.5
    elif "pp" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[int(index+(NUM_CLASSES/2))][4] = list[int(index+(NUM_CLASSES/2))-1][3]
            list[int(index+(NUM_CLASSES/2))][3] = list[int(index+(NUM_CLASSES/2))-1][2]
            list[int(index+(NUM_CLASSES/2))][2] = list[int(index+(NUM_CLASSES/2))-1][1]
            list[int(index+(NUM_CLASSES/2))][1] = list[int(index+(NUM_CLASSES/2))-1][0]
            list[int(index+(NUM_CLASSES/2))][0] = plays[int(index+(NUM_CLASSES/2))-1]
            NN_feature_shift(nn_list, rocks, papers, scissors, e_rocks, e_papers, e_scissors, index)
        plays[index] = 5
        plays[int(index+(NUM_CLASSES/2))] = 5
        papers[index] = 1
        papers[int(index+(NUM_CLASSES/2))] = 1
        e_papers[index] = 1
        e_papers[int(index+(NUM_CLASSES/2))] = 1
        labels[index] = 1
        labels[int(index+(NUM_CLASSES/2))] = 1
        list[index][5] = round
        list[int(index+(NUM_CLASSES/2))][5] = round
        nn_list[index][30] = (round+1)/10
        nn_list[int(index+(NUM_CLASSES/2))][30] = (round+1)/10
        if index != NUM_CLASSES-1 and index != (NUM_CLASSES/2)-1:
            list[index+1][6] += 0
            list[int(index+(NUM_CLASSES/2))+1][6] += 0
            nn_list[index+1][6] += 0
            nn_list[int(index+(NUM_CLASSES/2))+1][6] += 0
    elif "px" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[int(index+(NUM_CLASSES/2))][4] = list[int(index+(NUM_CLASSES/2))-1][3]
            list[int(index+(NUM_CLASSES/2))][3] = list[int(index+(NUM_CLASSES/2))-1][2]
            list[int(index+(NUM_CLASSES/2))][2] = list[int(index+(NUM_CLASSES/2))-1][1]
            list[int(index+(NUM_CLASSES/2))][1] = list[int(index+(NUM_CLASSES/2))-1][0]
            list[int(index+(NUM_CLASSES/2))][0] = plays[int(index+(NUM_CLASSES/2))-1]
            NN_feature_shift(nn_list, rocks, papers, scissors, e_rocks, e_papers, e_scissors, index)
        plays[index] = 6
        plays[int(index+(NUM_CLASSES/2))] = 8
        papers[index] = 1
        scissors[int(index+(NUM_CLASSES/2))] = 1
        e_scissors[index] = 1
        e_papers[int(index+(NUM_CLASSES/2))] = 1
        labels[index] = 1
        labels[int(index+(NUM_CLASSES/2))] = 2
        list[index][5] = round
        list[int(index+(NUM_CLASSES/2))][5] = round
        nn_list[index][30] = (round+1)/10
        nn_list[int(index+(NUM_CLASSES/2))][30] = (round+1)/10
        if index != NUM_CLASSES-1 and index != (NUM_CLASSES/2)-1:
            list[index+1][6] += -1
            list[int(index+(NUM_CLASSES/2))+1][6] += 1
            nn_list[index+1][6] += -0.5
            nn_list[int(index+(NUM_CLASSES/2))+1][6] += 0.5
    elif "xs" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[int(index+(NUM_CLASSES/2))][4] = list[int(index+(NUM_CLASSES/2))-1][3]
            list[int(index+(NUM_CLASSES/2))][3] = list[int(index+(NUM_CLASSES/2))-1][2]
            list[int(index+(NUM_CLASSES/2))][2] = list[int(index+(NUM_CLASSES/2))-1][1]
            list[int(index+(NUM_CLASSES/2))][1] = list[int(index+(NUM_CLASSES/2))-1][0]
            list[int(index+(NUM_CLASSES/2))][0] = plays[int(index+(NUM_CLASSES/2))-1]
            NN_feature_shift(nn_list, rocks, papers, scissors, e_rocks, e_papers, e_scissors, index)
        plays[index] = 7
        plays[int(index+(NUM_CLASSES/2))] = 3
        scissors[index] = 1
        rocks[int(index+(NUM_CLASSES/2))] = 1
        e_rocks[index] = 1
        e_scissors[int(index+(NUM_CLASSES/2))] = 1
        labels[index] = 2
        labels[int(index+(NUM_CLASSES/2))] = 0
        list[index][5] = round
        list[int(index+(NUM_CLASSES/2))][5] = round
        nn_list[index][30] = (round+1)/10
        nn_list[int(index+(NUM_CLASSES/2))][30] = (round+1)/10
        if index != NUM_CLASSES-1 and index != (NUM_CLASSES/2)-1:
            list[index+1][6] += -1
            list[int(index+(NUM_CLASSES/2))+1][6] += 1
            nn_list[index+1][6] += -0.5
            nn_list[int(index+(NUM_CLASSES/2))+1][6] += 0.5
    elif "xp" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[int(index+(NUM_CLASSES/2))][4] = list[int(index+(NUM_CLASSES/2))-1][3]
            list[int(index+(NUM_CLASSES/2))][3] = list[int(index+(NUM_CLASSES/2))-1][2]
            list[int(index+(NUM_CLASSES/2))][2] = list[int(index+(NUM_CLASSES/2))-1][1]
            list[int(index+(NUM_CLASSES/2))][1] = list[int(index+(NUM_CLASSES/2))-1][0]
            list[int(index+(NUM_CLASSES/2))][0] = plays[int(index+(NUM_CLASSES/2))-1]
            NN_feature_shift(nn_list, rocks, papers, scissors, e_rocks, e_papers, e_scissors, index)
        plays[index] = 8
        plays[int(index+(NUM_CLASSES/2))] = 6
        scissors[index] = 1
        papers[int(index+(NUM_CLASSES/2))] = 1
        e_papers[index] = 1
        e_scissors[int(index+(NUM_CLASSES/2))] = 1
        labels[index] = 2
        labels[int(index+(NUM_CLASSES/2))] = 1
        list[index][5] = round
        list[int(index+(NUM_CLASSES/2))][5] = round
        nn_list[index][30] = (round+1)/10
        nn_list[int(index+(NUM_CLASSES/2))][30] = (round+1)/10
        if index != NUM_CLASSES-1 and index != (NUM_CLASSES/2)-1:
            list[index+1][6] += 1
            list[int(index+(NUM_CLASSES/2))+1][6] += -1
            nn_list[index+1][6] += 0.5
            nn_list[int(index+(NUM_CLASSES/2))+1][6] += -0.5
    elif "xx" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[int(index+(NUM_CLASSES/2))][4] = list[int(index+(NUM_CLASSES/2))-1][3]
            list[int(index+(NUM_CLASSES/2))][3] = list[int(index+(NUM_CLASSES/2))-1][2]
            list[int(index+(NUM_CLASSES/2))][2] = list[int(index+(NUM_CLASSES/2))-1][1]
            list[int(index+(NUM_CLASSES/2))][1] = list[int(index+(NUM_CLASSES/2))-1][0]
            list[int(index+(NUM_CLASSES/2))][0] = plays[int(index+(NUM_CLASSES/2))-1]
            NN_feature_shift(nn_list, rocks, papers, scissors, e_rocks, e_papers, e_scissors, index)
        plays[index] = 9
        plays[int(index+(NUM_CLASSES/2))] = 9
        scissors[index] = 1
        scissors[int(index+(NUM_CLASSES/2))] = 1
        e_scissors[index] = 1
        e_scissors[int(index+(NUM_CLASSES/2))] = 1
        labels[index] = 2
        labels[int(index+(NUM_CLASSES/2))] = 2
        list[index][5] = round
        list[int(index+(NUM_CLASSES/2))][5] = round
        nn_list[index][30] = (round+1)/10
        nn_list[int(index+(NUM_CLASSES/2))][30] = (round+1)/10
        if index != NUM_CLASSES-1 and index != (NUM_CLASSES/2)-1:
            list[index+1][6] += 0
            list[int(index+(NUM_CLASSES/2))+1][6] += 0
            nn_list[index+1][6] += 0
            nn_list[int(index+(NUM_CLASSES/2))+1][6] += 0

    if round / 9 < 1:
        round += 1

    unique = False #just finished a play so not the first play in a game

    if "-" in line:
        round = 0
        unique = True #finished a game o best of 3 so next play is 1st play in a game
    else:
        index += 1 #already incremented before '-' so don't increment if '-'
print(list)
f.close()
np.save('data.npy', list)
np.save('NN_data.npy', nn_list)
np.save('labels.npy', labels)
array_reloaded = np.load('data.npy')
label_reloaded = np.load('labels.npy')
print(array_reloaded)
print(array_reloaded[0])
print(label_reloaded)
