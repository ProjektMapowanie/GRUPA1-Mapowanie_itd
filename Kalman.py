#import serial as serial
import math
import numpy as np

#sensorData= serial.Serial('com11',115200) # Create senorData object to read serial port data coming from arduino
import matplotlib.pyplot as plt

class Obserwator:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.dlugoscTablicy = 50
        self.mojaTablica = [[0 for col in range(self.dlugoscTablicy)] for row in range(self.dlugoscTablicy)]


    def wpisz (self, pomiar):
        self.mojaTablica[self.x][self.y + 1] = 15
        self.mojaTablica[self.x + 4 + int(round(pomiar[0]))][self.y] = 50
        self.mojaTablica[self.x - 1][self.y + int(round(pomiar[1])) + 5] = 50
        self.mojaTablica[self.x - 4 - int(round(pomiar[2]))][self.y - 1] = 50
        #self.mojaTablica[0][20] = 2


    def szachownica(self):

        for i in range(self.dlugoscTablicy):
            for j in range(self.dlugoscTablicy):
                if j%2 == 0 and i %2 == 0:
                    self.mojaTablica[i][j] = 99
                else:
                    self.mojaTablica[i][j] = 0


    def wpisz1(self, pomiar):
        zmianyx = [4, 0, -4]
        zmianyy = [0, 5, 0]
        for pom, zmx, zmy in zip (pomiar, zmianyx, zmianyy):
            self.mojaTablica[self.x + zmx][self.y + zmianyy + int(round(pom))] = 2
        self.mojaTablica[self.x][self.y] = 4



    def drukujTab(self):
        plt.imshow(self.mojaTablica, interpolation='nearest')
        plt.show()

    def wykonajRozkaz(self, rozkaz):
        if rozkaz == "g":
            self.x += 1
        if rozkaz == "p":
            self.y += 1




class Robot():
        def __init__(self):

            x = 0
            y = 0
            teta = 1.5708   #teta in radians, 90 degree
            self.X = np.transpose(np.matrix([x, y, teta]))
            self.PastStates = []
            self.landmark = ([[1, 2], [2,3]])


        def newStateB(self, V, w, dt): #velocity, rotation
            if not w == 0:
                x = V/w*math.sin(self.teta) + V/w*math.sin(self.teta + w*dt) #self.X[0] -    #teta in radians
                y = V/w*math.cos(self.teta) - V/w*math.cos(self.teta + w*dt) #self.X[1] +
                teta = w*dt #self.X[2] +
            else:
                x = round(V*dt*math.sin(self.X[2]), 2)# + self.X[0]
                y = round(V*dt*math.cos(self.X[2]), 2)# + self.X[1]
                teta = 0
            tab = np.matrix([x, y, teta])

            return np.transpose(tab)

        def newStateA(self):
            A = np.identity(3)
            #stan = np.transpose(np.array([self.x, self.y, self.teta]))
            return A*self.X

        def predictState(self):
            Bu = self.newStateB(1, 0, 1)
            Ax = self.newStateA()
            Xpredict = Ax + Bu
            return Xpredict

        def computeLandmarksFromSensors(self, pomiar):

            x1 = [self.X[0] + 4 + round(pomiar[0], 2), self.X[1]]
            x2 = [self.X[0] - 1][self.X[1] + round(pomiar[1], 2) + 5]
            x3 = [self.X[0] - 4 - round(pomiar[2], 2), self.X[1] - 1]
            self.landmark.append([x1, x2, x3])
            pass

        def predictObs(self, landmark):
            predictDistance = []            #mam watpliwosci czy to ma sens. Aktualnie estymujemy odleglosc miedzy pRobotem, a
                                            #wczesniej zmierzonymi landmarkami
                                            # i jakby to mialo wygladac? sprawdzamy, czy ktore sie pokrywa?
            for lm in landmark:
                predictDistance.append(math.sqrt((self.X[0] - lm[0])**2 + (self.X[1] - lm[1])**2))
            return predictDistance

        def aprioriCovarianceMatric(self):     #moze zamienic na klase lub fikusniej: funkcje z domknieciem
                                        #dekorator @cache?

            X = 0           #inicjalizacja
            Y = 0
            teta = 0
                #dla xow
            Exx = 0
            Exy = 0
            Ext = 0
                #dla yow
            Eyy = 0
            Eyt = 0
                #dla xow
            Ett = 0

            for state in self.PastStates:       #licz i sumuj tak by bylo to co potrzebne
                                                #state : 0 - x, 1 - y,  2 - z
                X = X + state[0]
                Y = Y + state[1]
                teta = teta + state[2]

                Exx = Exx + state[0]**2
                Exy = Exy + state[0]*state[1]
                Ext = Ext + state[0]*state[2]

                Eyy = Eyy + state[1]*state[1]
                Eyt = Eyt + state[1]*state[2]

                Ett = Ett + state[2]*state[2]

            aX = X/self.PastStates.__len__()
            aY = Y/self.PastStates.__len__()
            aT = teta/self.PastStates.__len__()

            covxx = Exx - aX**2
            covxy = Exy - aX*aY
            covxt = Ext - aX*aT

            covyy = Eyy - aY**2
            covyt = Eyt - aY*aT

            covtt = Ett - aT**2

            return np.matrix([[covxx, covxy, covxt],
                             [covxy, covyy, covyt],
                             [covxt, covyt, covtt]])


        def Step(self):
            self.PastStates = [[0, 1, self.X[2]], [0, 3, self.X[2]], [0, 2, self.X[2]]]

            #predict step

            Xpredict = self.predictState()
            Zpredict = self.predictObs(self.landmark)
            Epredict = self.aprioriCovarianceMatric()   #to ze wzoru, czy z AEA + R???



def recv():
    pass



def main():
    robot = Robot()
    robot.predictState()
    robot.Step()


if __name__ == "__main__":
    main()


def starymain():
    sensorData = serial.Serial('COM4', 9600)
    obserw = Obserwator()

    plik = open('plik.txt', 'w')

    i = 0
    rozkaz =raw_input("podaj rozkaz:")
    while (rozkaz != "q"):
        while(sensorData.inWaiting()==0): # Wait here untill there is data on the Serial Port
            pass                          # Do nothing, just loop until data arrives

        textline = sensorData.readline()     # read the entire line of text
        dataNums=textline.split(',')       #Remember to split the line of text into an array at the commas


        print textline
        #print dataNums[0], dataNums[2], dataNums[4]      # Make variables for Red, Blue, Green. Remember
        #obserw.wpisz([float(dataNums[0]), float(dataNums[2]), float(dataNums[4])])
        tekst = textline +"\n"
        plik.write(tekst)
        rozkaz =raw_input("podaj rozkaz")
        if rozkaz != "q":
            obserw.wykonajRozkaz(rozkaz)

        sensorData.reset_input_buffer()

    plik.close()
    obserw.drukujTab()
