import serial as serial
import time

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



def Robot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.V = 0
        self.teta = 0

def main():

    pass


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
