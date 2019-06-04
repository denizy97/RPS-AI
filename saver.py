import pandas as pd
import numpy as np
#data = pd.read_excel("data.xlsx")
#print(data)
#np.save('data.npy', data)
#array_reloaded = np.load('data.npy')
#print(array_reloaded)
#print(array_reloaded[1][3])
list = np.zeros((1530, 12))
labels = np.zeros((1530))
f = open("data.txt", "r")
index = 0
round = 1
unique = True
for line in f:
    if "ss" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = labels[index-1]
        labels[index] = 1
        list[index][5] = round
        list[index][6] += 0
    elif "sp" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = labels[index-1]
        labels[index] = 2
        list[index][5] = round
        list[index][6] += -1
    elif "sx" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = labels[index-1]
        labels[index] = 3
        list[index][5] = round
        list[index][6] += 1
    elif "ps" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = labels[index-1]
        labels[index] = 4
        list[index][5] = round
        list[index][6] += 1
    elif "pp" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = labels[index-1]
        labels[index] = 5
        list[index][5] = round
        list[index][6] += 0
    elif "px" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = labels[index-1]
        labels[index] = 6
        list[index][5] = round
        list[index][6] += -1
    elif "xs" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = labels[index-1]
        labels[index] = 7
        list[index][5] = round
        list[index][6] += -1
    elif "xp" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = labels[index-1]
        labels[index] = 8
        list[index][5] = round
        list[index][6] += 1
    elif "xx" in line:
        if index != 0 and not unique:
            list[index][4] = list[index-1][3]
            list[index][3] = list[index-1][2]
            list[index][2] = list[index-1][1]
            list[index][1] = list[index-1][0]
            list[index][0] = labels[index-1]
        labels[index] = 9
        list[index][5] = round
        list[index][6] += 0
    if round / 10 < 1:
        round += 1
    unique = False
    if "-" in line:
        round = 1
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
print(label_reloaded)
