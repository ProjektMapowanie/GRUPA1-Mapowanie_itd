# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


#from __future__ import unicode_literals
import sys
import os
import random
from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE

from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import math as m


progname = os.path.basename(sys.argv[0])
progversion = "0.1"




class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(856, 539)
        self.widget = QtGui.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(170, 10, 671, 511))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton = QtGui.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 141, 81))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 141, 81))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalSlider = QtGui.QSlider(Widget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 240, 121, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.pushButton.setText(_translate("Widget", "PushButton", None))
        self.pushButton_2.setText(_translate("Widget", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

