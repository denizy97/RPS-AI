import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = np.load('data.npy')
neural_data = np.load('NN_data.npy')
labels = np.load('labels.npy')
data_featurenames = ("play0", "play1", "play2", "play3", "play4", "round", "score")
neural_featurenames = ("meR0", "meP0", "meS0", "enemyR0", "enemyP0", "enemyS0", "meR1", "meP1", "meS1", "enemyR1", "enemyP1", "enemyS1",
                        "meR2", "meP2", "meS2", "enemyR2", "enemyP2", "enemyS2", "meR3", "meP3", "meS3", "enemyR3", "enemyP3", "enemyS3",
                        "meR4", "meP4", "meS4", "enemyR4", "enemyP4", "enemyS4", "round", "score")

#for idx in range(len(data_featurenames)):
#    for idx2 in range(idx+1, len(data_featurenames)):
#        plt.figure()
#        plt.xlabel(data_featurenames[idx])
#        plt.ylabel(data_featurenames[idx2])
#        rocks_x = []
#        papers_x = []
#        scissors_x = []
#        rocks_y = []
#        papers_y = []
#        scissors_y = []
#        for label_idx in range(len(labels)):
#            if labels[label_idx] == 0:
#                rocks_x.append(data[label_idx][idx])
#                rocks_y.append(data[label_idx][idx2])
#            if labels[label_idx] == 1:
#                scissors_x.append(data[label_idx][idx]+0.1)
#                scissors_y.append(data[label_idx][idx2]+0.1)
#            if labels[label_idx] == 2:
#                papers_x.append(data[label_idx][idx]+0.2)
#                papers_y.append(data[label_idx][idx2]+0.2)
#        plt.scatter(rocks_x,rocks_y, color='gray')
#        plt.scatter(papers_x,papers_y, color='green')
#        plt.scatter(scissors_x,scissors_y, color='red')
#        plt.show()


for idx in range(len(neural_featurenames)):
    rocks = np.zeros(10)
    papers = np.zeros(10)
    scissors = np.zeros(10)
    for label_idx in range(len(labels)):
        if idx < 30:
            value = int(neural_data[label_idx][idx])
        elif idx == 30:
            value = int(neural_data[label_idx][idx]*10-1)
        elif idx == 31:
            value = int(neural_data[label_idx][idx]*2+2)
        if labels[label_idx] == 0:
            rocks[value] += 1
        if labels[label_idx] == 1:
            papers[value] += 1
        if labels[label_idx] == 2:
            scissors[value] += 1
    for i in range(10):
        sum = rocks[i]+papers[i]+scissors[i]
        rocks[i] = rocks[i]/sum
        papers[i] = papers[i]/sum
        scissors[i] = scissors[i]/sum
    plt.figure()
    plt.xlabel(neural_featurenames[idx])
    plt.ylabel('Amount')
    plt.plot(rocks, label='Rock')
    plt.plot(papers, label = 'Paper')
    plt.plot(scissors, label = 'Scissor')
    plt.legend()
    plt.show()
