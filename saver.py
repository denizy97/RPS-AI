import pandas as pd
import numpy as np
#data = pd.read_excel("data.xlsx")
#print(data)
#np.save('data.npy', data)
#array_reloaded = np.load('data.npy')
#print(array_reloaded)
#print(array_reloaded[1][3])
list = np.zeros((3060, 12), dtype = int)
labels = np.zeros((3060), dtype = int)
plays = np.zeros((3060), dtype = int)
list[:, 6] = 2
f = open("data.txt", "r")
index = 0
round = 0
unique = True
for line in f:
    if "ss" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[index+1530][4] = list[index+1530-1][3]
            list[index+1530][3] = list[index+1530-1][2]
            list[index+1530][2] = list[index+1530-1][1]
            list[index+1530][1] = list[index+1530-1][0]
            list[index+1530][0] = plays[index+1530-1]
        plays[index] = 1
        plays[index+1530] = 1
        labels[index] = 1
        labels[index+1530] = 1
        list[index][5] = round
        list[index][6] += 0
        list[index+1530][5] = round
        list[index+1530][6] += 0
    elif "sp" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[index+1530][4] = list[index+1530-1][3]
            list[index+1530][3] = list[index+1530-1][2]
            list[index+1530][2] = list[index+1530-1][1]
            list[index+1530][1] = list[index+1530-1][0]
            list[index+1530][0] = plays[index+1530-1]
        plays[index] = 2
        plays[index+1530] = 4
        labels[index] = 1
        labels[index+1530] = 2
        list[index][5] = round
        list[index][6] += -1
        list[index+1530][5] = round
        list[index+1530][6] += 1
    elif "sx" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[index+1530][4] = list[index+1530-1][3]
            list[index+1530][3] = list[index+1530-1][2]
            list[index+1530][2] = list[index+1530-1][1]
            list[index+1530][1] = list[index+1530-1][0]
            list[index+1530][0] = plays[index+1530-1]
        plays[index] = 3
        plays[index+1530] = 7
        labels[index] = 1
        labels[index+1530] = 3
        list[index][5] = round
        list[index][6] += 1
        list[index+1530][5] = round
        list[index+1530][6] += -1
    elif "ps" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[index+1530][4] = list[index+1530-1][3]
            list[index+1530][3] = list[index+1530-1][2]
            list[index+1530][2] = list[index+1530-1][1]
            list[index+1530][1] = list[index+1530-1][0]
            list[index+1530][0] = plays[index+1530-1]
        plays[index] = 4
        plays[index+1530] = 2
        labels[index] = 2
        labels[index+1530] = 1
        list[index][5] = round
        list[index][6] += 1
        list[index+1530][5] = round
        list[index+1530][6] += -1
    elif "pp" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[index+1530][4] = list[index+1530-1][3]
            list[index+1530][3] = list[index+1530-1][2]
            list[index+1530][2] = list[index+1530-1][1]
            list[index+1530][1] = list[index+1530-1][0]
            list[index+1530][0] = plays[index+1530-1]
        plays[index] = 5
        plays[index+1530] = 5
        labels[index] = 2
        labels[index+1530] = 2
        list[index][5] = round
        list[index][6] += 0
        list[index+1530][5] = round
        list[index+1530][6] += 0
    elif "px" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[index+1530][4] = list[index+1530-1][3]
            list[index+1530][3] = list[index+1530-1][2]
            list[index+1530][2] = list[index+1530-1][1]
            list[index+1530][1] = list[index+1530-1][0]
            list[index+1530][0] = plays[index+1530-1]
        plays[index] = 6
        plays[index+1530] = 8
        labels[index] = 2
        labels[index+1530] = 3
        list[index][5] = round
        list[index][6] += -1
        list[index+1530][5] = round
        list[index+1530][6] += 1
    elif "xs" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[index+1530][4] = list[index+1530-1][3]
            list[index+1530][3] = list[index+1530-1][2]
            list[index+1530][2] = list[index+1530-1][1]
            list[index+1530][1] = list[index+1530-1][0]
            list[index+1530][0] = plays[index+1530-1]
        plays[index] = 7
        plays[index+1530] = 3
        labels[index] = 3
        labels[index+1530] = 1
        list[index][5] = round
        list[index][6] += -1
        list[index+1530][5] = round
        list[index+1530][6] += 1
    elif "xp" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[index+1530][4] = list[index+1530-1][3]
            list[index+1530][3] = list[index+1530-1][2]
            list[index+1530][2] = list[index+1530-1][1]
            list[index+1530][1] = list[index+1530-1][0]
            list[index+1530][0] = plays[index+1530-1]
        plays[index] = 8
        plays[index+1530] = 6
        labels[index] = 3
        labels[index+1530] = 2
        list[index][5] = round
        list[index][6] += 1
        list[index+1530][5] = round
        list[index+1530][6] += -1
    elif "xx" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = plays[index-1]
            list[index+1530][4] = list[index+1530-1][3]
            list[index+1530][3] = list[index+1530-1][2]
            list[index+1530][2] = list[index+1530-1][1]
            list[index+1530][1] = list[index+1530-1][0]
            list[index+1530][0] = plays[index+1530-1]
        plays[index] = 9
        plays[index+1530] = 9
        labels[index] = 3
        labels[index+1530] = 3
        list[index][5] = round
        list[index][6] += 0
        list[index+1530][5] = round
        list[index+1530][6] += 0
    if index == 1338:
        print(line)
    if round / 9 < 1:
        round += 1
    unique = False
    if "-" in line:
        round = 0
        unique = True
    else:
        index += 1
print(list)
f.close()
np.save('data.npy', list)
np.save('labels.npy', labels)
array_reloaded = np.load('data.npy')
label_reloaded = np.load('labels.npy')
print(array_reloaded)
print(array_reloaded[0])
print(label_reloaded[1338])
