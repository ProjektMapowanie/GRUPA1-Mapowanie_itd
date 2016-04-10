import matplotlib.pyplot as plt
import numpy as np
import random
import math

x = np.arange(6)
y = np.arange(5)
z = x * y[:, np.newaxis]

i = 0

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.teta = 1.5708   #teta in radians, 90 degree
        self.X = np.matrix([0, 0, 1.5708])#np.transpose(np.matrix([0, 0, 1.5708]))
        self.PastStates = []
        self.landmark = ([[1, 2], [2,3]])
        self.X = np.transpose(np.matrix([0, 0, 1.5708]))
        print(self.X[0].item)


    def paint(self, plt):
        arm = 0.6
        angle30 = math.radians(30) # self.X.item(2)
        angle60 = math.radians(60)
        plt.clf()
        x = self.X.item(0)
        y = self.X.item(1)
        teta = self.X.item(2)
        Am = [x + arm*math.cos(teta), x + arm*math.cos(angle30), x - arm*math.cos(angle30), x + arm*math.cos(teta)]
        Am = [y + arm*math.sin(teta) + arm*math.sin(teta), y - arm*math.sin(angle30), y - arm*math.sin(angle30),
              y + arm*math.sin(teta) + arm*math.sin(teta)]

        Ax = [x + arm*math.cos(teta),
              x + arm*math.cos(teta) - 1.5*arm*math.sin(angle60 - teta),
              x + arm*math.cos(teta) - 1.5*arm*math.sin(angle60 - teta) - 1.5*arm*math.sin(teta),
              x + arm*math.cos(teta)]
        Ay = [y + arm*math.sin(teta),
              y + arm*math.sin(teta) - 1.5*arm*math.cos(angle60 - teta),
              y + arm*math.sin(teta) - 1.5*arm*math.cos(angle60 - teta) + 1.5*arm*math.cos(teta),
              y + arm*math.sin(teta)]
        plt.fill(Ax, Ay)
        plt.plot([-1, 9],[-1, 9])
        pass

    def updateRobotState(self):
        self.X[0] = self.X[0] + 0.1
        self.X[1] = self.X[1] + 0.1
        self.X[2] = self.X[2] + 0.1


def main():
    robot = Robot()
    wektor = [[1,2,3],[2,3,5], [3, 4, 2]]
    i = 0
    while(True):


        robot.paint(plt)
        robot.updateRobotState()
        plt.title("Boring slide show")
        print("step", i)
        plt.pause(0.5)


if __name__ == "__main__":
    main()