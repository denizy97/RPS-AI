import numpy as np
class Q_Agent:

    def __init__(self, actions, Ne, C, gamma):
        self.actions = actions
        self.Ne = Ne # used in exploration function
        self.C = C
        self.gamma = gamma
        self.reset()
        # Create the Q and N Table to work with
        self.Q = np.zeros((10,10,10,10,10,10,5,2,7))
        self.N = np.zeros((10,10,10,10,10,10,5,2,7))

    def train(self):
        self._train = True

    def eval(self):
        self._train = False

    def reset(self):
        self.points = 0
        self.s = None
        self.a = None

    def train(self, train_set, train_label):
        for index in range(train_set.shape[0]):
            sPrime = tuple(train_set[index].tolist())
            rewardS = (train_set[index][6] - 2) - self.points
            self.points = train_set[index][6] - 2
            if self.s != None and self.a != None:
                nextActionQ = np.amax(self.Q[sPrime])
                self.N[self.s][self.a] += 1
                alpha = self.C / (self.C + self.N[self.s][self.a])
                self.Q[self.s][self.a] = self.Q[self.s][self.a] + alpha * (rewardS + self.gamma * nextActionQ - self.Q[self.s][self.a])
            if index < train_set.shape[0] and train_set[index+1][0] != 0:
                self.a = (train_set[index+1][0] - 1) / 3
                self.s = sPrime
            else:
                self.reset()

    def act(self, state, label):
        sPrime = tuple(state.tolist())
        if self._train == True:
            rewardS = (state[6] - 2) - self.points
            self.points = state[6] - 2
            if self.s != None and self.a != None:
                nextActionQ = np.amax(self.Q[sPrime])
                self.N[self.s][self.a] += 1
                alpha = self.C / (self.C + self.N[self.s][self.a])
                self.Q[self.s][self.a] = self.Q[self.s][self.a] + alpha * (rewardS + self.gamma * nextActionQ - self.Q[self.s][self.a])
            #nextAction = 3
            nextActionQ = float('-inf')
            tempQ = np.empty_like(self.Q[sPrime])
            tempQ = np.where(self.N[sPrime] < self.Ne, 1, self.Q[sPrime])
            for a in range(len(tempQ)):
                if tempQ[a] >= nextActionQ:
                    nextAction = a
                    nextActionQ = tempQ[a]
            self.a = nextAction
            self.s = sPrime
            if state[0] == 0:
                self.reset()

        elif self._train == False:
            nextAction = 0
            nextActionQ = float('-inf')
            for a in range(3):
                if self.Q[sPrime][a] >= nextActionQ:
                    nextAction = a
                    nextActionQ = self.Q[sPrime][a]
        return self.actions[nextAction]
