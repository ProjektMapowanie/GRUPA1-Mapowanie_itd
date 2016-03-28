
from __future__ import unicode_literals
import sys, os


progname = os.path.basename(sys.argv[0])
progversion = "0.1"

import random
import sys
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure
import serial as serial
import sys, random
import time
sensorData = serial.Serial('COM4',9600)     #115200)
import matplotlib.pyplot as plt
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QMainWindow, QApplication


class Obserwator:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.dlugoscTablicy = 50
        self.mojaTablica = [[0 for col in range(self.dlugoscTablicy)] for row in range(self.dlugoscTablicy)]


    def wpisz1 (self, pomiar):
        zmianyx = [4 +  pomiar[0], -1, -4 - pomiar[2]]
        zmianyy = [0, pomiar[1] + 5, -1]

        for zx, zy, pom in range(zip (zmianyx, zmianyy, pomiar)):
            if pom < 30:
                self.mojaTablica[self.x + zx][self.y + zy] = 20


    def szachownica(self):

        for i in range(self.dlugoscTablicy):
            for j in range(self.dlugoscTablicy):
                if j%2 == 0 and i %2 == 0:
                    self.mojaTablica[i][j] = 4.25
                else:
                    self.mojaTablica[i][j] = 6.4


    def wpisz(self, pomiar):
        self.mojaTablica[self.x][self.y] = 15 #nie wiem czy to : + 1] = 15 mialo jakis sens

        self.mojaTablica[self.x + 4 + int(round(pomiar[0]))][self.y] = 20
        self.mojaTablica[self.x - 1][self.y + int(round(pomiar[1])) + 5] = 20
        self.mojaTablica[self.x - 4 - int(round(pomiar[2]))][self.y - 1] = 20



    def drukujTab(self):
        plt.imshow(self.mojaTablica, interpolation='nearest')
        plt.show()

    def wykonajRozkaz(self, rozkaz):
        if rozkaz == "g":
            self.x += 1
        if rozkaz == "p":
            self.y += 1

obserw = Obserwator()
obserw.szachownica()

class Robot(QMainWindow):

    def dzialanie(self):
    #while True: #This is a while loop that will loop forever, since True is always True.

        obserw = self.Obserwator()
        obserw.szachownica()


        i = 0
        rozkaz =raw_input("podaj rozkaz")
        while (rozkaz != "q"):
            while(sensorData.inWaiting()==0): # Wait here untill there is data on the Serial Port
                pass                          # Do nothing, just loop until data arrives

            textline = sensorData.readline()     # read the entire line of text
            dataNums=textline.split(',')       #Remember to split the line of text into an array at the commas

            print textline
            print dataNums[0], dataNums[2], dataNums[4]  # Make variables for Red, Blue, Green. Remember
            obserw.wpisz([int(round(float(dataNums[0])), int(round(float(dataNums[2]))), int(round(float(dataNums[4]))) )])

            rozkaz =raw_input("podaj rozkaz")
            if rozkaz != "q":
                obserw.wykonajRozkaz(rozkaz)
            sensorData.close()
        obserw.drukujTab()



    class MyDynamicMplCanvas(FigureCanvas):
        """A canvas that updates itself every second with a new plot."""
        def __init__(self, parent=None, width=5, height=4, dpi=100):
            fig = Figure(figsize=(width, height), dpi=dpi)
            self.axes = fig.add_subplot(111)
            # We want the axes cleared every time plot() is called
            self.axes.hold(False)

            self.compute_initial_figure()

            #
            FigureCanvas.__init__(self, fig)
            self.setParent(parent)

            FigureCanvas.setSizePolicy(self,
                                       QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Expanding)
            FigureCanvas.updateGeometry(self)
            #super(self, *args, **kwargs)
            timer = QtCore.QTimer(self)
            QtCore.QObject.connect(timer, QtCore.SIGNAL("timeout()"), self.update_figure)
            timer.start(1000)

        def compute_initial_figure(self):
             self.axes.imshow(obserw.mojaTablica, interpolation='nearest')




        def update_figure(self):

            textline = sensorData.readline()     # read the entire line of text
            dataNums=textline.split(',')       #Remember to split the line of text into an array at the commas


            print textline
            print dataNums[0], dataNums[2], dataNums[4]      # Make variables for Red, Blue, Green. Remember
            obserw.wpisz([float(dataNums[0]), float(dataNums[2]), float(dataNums[4])])

            sensorData.reset_input_buffer()

            self.axes.imshow(obserw.mojaTablica, interpolation='nearest')
            self.draw()#plt.show()



    def __init__(self, parent=None):

        QMainWindow.__init__(self)
        self.ui = QMainWindow()
        uic.loadUi('untitled.ui', self)
        l = self.layout()

        sc = self.MyDynamicMplCanvas(self.ui, width=8, height=4, dpi=100)
        #sc = self.MyDynamicMplCanvas(self.ui, width=6, height=6, dpi=100)
        l.addWidget(sc)
        #sc = self.MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)

        self.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Robot()
    myapp.show()
    sys.exit(app.exec_())