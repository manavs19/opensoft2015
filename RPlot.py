# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPlot.ui'
#
# Created: Tue Mar 10 16:35:23 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 581, 501))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
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
        RPlot.setWindowTitle(QtGui.QApplication.translate("RPlot", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RPlot", "Expression:", None, QtGui.QApplication.UnicodeUTF8))
        self.Plot.setText(QtGui.QApplication.translate("RPlot", "Plot", None, QtGui.QApplication.UnicodeUTF8))

