# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPlot.ui'
#
# Created: Wed Mar 11 01:34:54 2015
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
    def get_values(self):
        try:
            x_min = float(self.lineEdit_x_min.text())
            x_max = float(self.lineEdit_x_max.text())
            no_of_pts = int(self.lineEdit_pts.text())
            return (x_min, x_max, no_of_pts)
        except ValueError:
            print "One of the params is not in the desired format"
    def sin_pressed(self):
        x_min, x_max, no_of_points = self.get_values()
        x2 = np.linspace(x_min, x_max, no_of_points)
        data2 = np.sin(x2)
        self.w1.plot(x2, data2, pen=(255,255,255,200))
    def cos_pressed(self):
		x_min, x_max, no_of_points = self.get_values()
		x2 = np.linspace(x_min, x_max, no_of_points)
		data2 = np.cos(x2)
		self.w1.plot(x2, data2, pen=(255,0,0,200))
    def square_pressed(self):
		x_min, x_max, no_of_points = self.get_values()
		x2 = np.linspace(x_min, x_max, no_of_points)
		data2 = x2 ** 2
		self.w1.plot(x2, data2, pen=(0,255,0,200))
    def setupUi(self, RPlot):
        RPlot.setObjectName(_fromUtf8("RPlot"))
        RPlot.resize(800, 600)
        self.centralwidget = QtGui.QWidget(RPlot)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(633, 70, 161, 71))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(634, 40, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.Plot_sin = QtGui.QPushButton(self.centralwidget)
        self.Plot_sin.setGeometry(QtCore.QRect(650, 310, 98, 27))
        self.Plot_sin.setObjectName(_fromUtf8("Plot_sin"))
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 581, 501))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.Plot_cos = QtGui.QPushButton(self.centralwidget)
        self.Plot_cos.setGeometry(QtCore.QRect(650, 350, 98, 27))
        self.Plot_cos.setObjectName(_fromUtf8("Plot_cos"))
        self.Plot_2 = QtGui.QPushButton(self.centralwidget)
        self.Plot_2.setGeometry(QtCore.QRect(650, 390, 98, 27))
        self.Plot_2.setObjectName(_fromUtf8("Plot_2"))
        self.label_x_min = QtGui.QLabel(self.centralwidget)
        self.label_x_min.setGeometry(QtCore.QRect(630, 160, 101, 17))
        self.label_x_min.setObjectName(_fromUtf8("label_x_min"))
        self.label_x_max = QtGui.QLabel(self.centralwidget)
        self.label_x_max.setGeometry(QtCore.QRect(630, 210, 101, 17))
        self.label_x_max.setObjectName(_fromUtf8("label_x_max"))
        self.label_pts = QtGui.QLabel(self.centralwidget)
        self.label_pts.setGeometry(QtCore.QRect(638, 250, 101, 17))
        self.label_pts.setObjectName(_fromUtf8("label_pts"))
        self.lineEdit_x_min = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_x_min.setGeometry(QtCore.QRect(680, 155, 113, 27))
        self.lineEdit_x_min.setObjectName(_fromUtf8("lineEdit_x_min"))
        self.lineEdit_x_max = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_x_max.setGeometry(QtCore.QRect(680, 205, 113, 27))
        self.lineEdit_x_max.setObjectName(_fromUtf8("lineEdit_x_max"))
        self.lineEdit_pts = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_pts.setGeometry(QtCore.QRect(708, 244, 71, 27))
        self.lineEdit_pts.setObjectName(_fromUtf8("lineEdit_pts"))
        self.w1 = self.graphicsView.addPlot()
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
        self.label_x_min.setText(_translate("RPlot", "x_min:", None))
        self.label_x_max.setText(_translate("RPlot", "x_max:", None))
        self.label_pts.setText(_translate("RPlot", "no of pts:", None))

from pyqtgraph import GraphicsLayoutWidget
