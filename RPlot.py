# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPlot.ui'
#
# Created: Tue Mar 10 19:48:42 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np

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

class Ui_RPlot(object):
    def sin_pressed(self):
        x2 = np.linspace(-5, 5, 1000)
        data2 = np.sin(x2)
        self.w1.plot(data2, pen=(255,255,255,200))
    def cos_pressed(self):
        x2 = np.linspace(-5, 5, 1000)
        data2 = np.cos(x2)
        self.w1.plot(data2, pen=(255,0,0,200))
    def square_pressed(self):
        x2 = np.linspace(-5, 5, 1000)
        data2 = x2 ** 2
        self.w1.plot(data2, pen=(0,255,0,200))
    def setupUi(self, RPlot):
        RPlot.setObjectName(_fromUtf8("RPlot"))
        RPlot.resize(800, 600)
        self.centralwidget = QtGui.QWidget(RPlot)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(620, 70, 161, 71))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 40, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.Plot_sin = QtGui.QPushButton(self.centralwidget)
        self.Plot_sin.setGeometry(QtCore.QRect(650, 220, 98, 27))
        self.Plot_sin.setObjectName(_fromUtf8("Plot_sin"))
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 581, 501))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.w1 = self.graphicsView.addPlot()
        self.Plot_cos = QtGui.QPushButton(self.centralwidget)
        self.Plot_cos.setGeometry(QtCore.QRect(650, 260, 98, 27))
        self.Plot_cos.setObjectName(_fromUtf8("Plot_cos"))
        self.Plot_2 = QtGui.QPushButton(self.centralwidget)
        self.Plot_2.setGeometry(QtCore.QRect(650, 300, 98, 27))
        self.Plot_2.setObjectName(_fromUtf8("Plot_2"))
        RPlot.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RPlot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        RPlot.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(RPlot)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        RPlot.setStatusBar(self.statusBar)

        self.retranslateUi(RPlot)
        QtCore.QObject.connect(self.Plot_sin, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sin_pressed)
        QtCore.QObject.connect(self.Plot_cos, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cos_pressed)
        QtCore.QObject.connect(self.Plot_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.square_pressed)
        QtCore.QMetaObject.connectSlotsByName(RPlot)

    def retranslateUi(self, RPlot):
        RPlot.setWindowTitle(_translate("RPlot", "MainWindow", None))
        self.label.setText(_translate("RPlot", "Expression:", None))
        self.Plot_sin.setText(_translate("RPlot", "Plot sin", None))
        self.Plot_cos.setText(_translate("RPlot", "Plot cos", None))
        self.Plot_2.setText(_translate("RPlot", "Plot x^2", None))

from pyqtgraph import GraphicsLayoutWidget
