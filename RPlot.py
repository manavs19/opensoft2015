# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPlot.ui'
#
# Created: Tue Mar 10 19:31:35 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np
import pyqtgraph as pg

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
        self.Plot = QtGui.QPushButton(self.centralwidget)
        self.Plot.setGeometry(QtCore.QRect(650, 220, 98, 27))
        self.Plot.setObjectName(_fromUtf8("Plot"))
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 581, 501))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        
        w1 = self.graphicsView.addPlot()
        
        x2 = np.linspace(-100, 100, 1000)
        data2 = x2 ** 2
        data3 = (x2 - 25 )** 2
        
        w1.plot(data3, pen=(255,0,0,200))
        w1.plot(data2, pen=(255,255,255,200))
        
        RPlot.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RPlot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        RPlot.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(RPlot)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        RPlot.setStatusBar(self.statusBar)

        self.retranslateUi(RPlot)
        QtCore.QMetaObject.connectSlotsByName(RPlot)

    def retranslateUi(self, RPlot):
        RPlot.setWindowTitle(_translate("RPlot", "MainWindow", None))
        self.label.setText(_translate("RPlot", "Expression:", None))
        self.Plot.setText(_translate("RPlot", "Plot", None))

from pyqtgraph import GraphicsLayoutWidget
