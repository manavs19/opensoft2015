# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPlot.ui'
#
# Created: Wed Mar 11 12:59:26 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_RPlot(object):
    def setupUi(self, RPlot):
        RPlot.setObjectName(_fromUtf8("RPlot"))
        RPlot.resize(800, 600)
        self.centralwidget = QtGui.QWidget(RPlot)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, 10, 781, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit_x_max = QtGui.QLineEdit(self.tab)
        self.lineEdit_x_max.setGeometry(QtCore.QRect(650, 204, 113, 27))
        self.lineEdit_x_max.setObjectName(_fromUtf8("lineEdit_x_max"))
        self.label_x_max = QtGui.QLabel(self.tab)
        self.label_x_max.setGeometry(QtCore.QRect(600, 210, 101, 17))
        self.label_x_max.setObjectName(_fromUtf8("label_x_max"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(603, 70, 161, 71))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(604, 40, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.Plot_cos = QtGui.QPushButton(self.tab)
        self.Plot_cos.setGeometry(QtCore.QRect(620, 350, 98, 27))
        self.Plot_cos.setObjectName(_fromUtf8("Plot_cos"))
        self.label_x_min = QtGui.QLabel(self.tab)
        self.label_x_min.setGeometry(QtCore.QRect(600, 160, 101, 17))
        self.label_x_min.setObjectName(_fromUtf8("label_x_min"))
        self.Plot_2 = QtGui.QPushButton(self.tab)
        self.Plot_2.setGeometry(QtCore.QRect(620, 390, 98, 27))
        self.Plot_2.setObjectName(_fromUtf8("Plot_2"))
        self.label_pts = QtGui.QLabel(self.tab)
        self.label_pts.setGeometry(QtCore.QRect(608, 250, 101, 17))
        self.label_pts.setObjectName(_fromUtf8("label_pts"))
        self.graphicsView = GraphicsLayoutWidget(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(2, 6, 581, 501))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.lineEdit_x_min = QtGui.QLineEdit(self.tab)
        self.lineEdit_x_min.setGeometry(QtCore.QRect(650, 155, 113, 27))
        self.lineEdit_x_min.setObjectName(_fromUtf8("lineEdit_x_min"))
        self.Plot_sin = QtGui.QPushButton(self.tab)
        self.Plot_sin.setGeometry(QtCore.QRect(620, 310, 98, 27))
        self.Plot_sin.setObjectName(_fromUtf8("Plot_sin"))
        self.lineEdit_pts = QtGui.QLineEdit(self.tab)
        self.lineEdit_pts.setGeometry(QtCore.QRect(678, 244, 71, 27))
        self.lineEdit_pts.setObjectName(_fromUtf8("lineEdit_pts"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.Plot_surface = QtGui.QPushButton(self.tab_2)
        self.Plot_surface.setGeometry(QtCore.QRect(617, 400, 131, 27))
        self.Plot_surface.setObjectName(_fromUtf8("Plot_surface"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(604, 40, 101, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_x_min_3d = QtGui.QLabel(self.tab_2)
        self.label_x_min_3d.setGeometry(QtCore.QRect(600, 160, 51, 17))
        self.label_x_min_3d.setObjectName(_fromUtf8("label_x_min_3d"))
        self.graphicsView_3d = GLViewWidget(self.tab_2)
        self.graphicsView_3d.setGeometry(QtCore.QRect(2, 6, 581, 501))
        self.graphicsView_3d.setObjectName(_fromUtf8("graphicsView_3d"))
        self.plainTextEdit_3d = QtGui.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_3d.setGeometry(QtCore.QRect(603, 70, 161, 71))
        self.plainTextEdit_3d.setObjectName(_fromUtf8("plainTextEdit_3d"))
        self.lineEdit_pts_3d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_pts_3d.setGeometry(QtCore.QRect(678, 304, 71, 27))
        self.lineEdit_pts_3d.setObjectName(_fromUtf8("lineEdit_pts_3d"))
        self.lineEdit_x_min_3d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_x_min_3d.setGeometry(QtCore.QRect(650, 155, 113, 27))
        self.lineEdit_x_min_3d.setObjectName(_fromUtf8("lineEdit_x_min_3d"))
        self.label_pts_3d = QtGui.QLabel(self.tab_2)
        self.label_pts_3d.setGeometry(QtCore.QRect(608, 310, 71, 17))
        self.label_pts_3d.setObjectName(_fromUtf8("label_pts_3d"))
        self.lineEdit_x_max_3d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_x_max_3d.setGeometry(QtCore.QRect(650, 184, 113, 27))
        self.lineEdit_x_max_3d.setObjectName(_fromUtf8("lineEdit_x_max_3d"))
        self.label_x_max_3d = QtGui.QLabel(self.tab_2)
        self.label_x_max_3d.setGeometry(QtCore.QRect(600, 190, 51, 17))
        self.label_x_max_3d.setObjectName(_fromUtf8("label_x_max_3d"))
        self.lineEdit_y_min_3d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_y_min_3d.setGeometry(QtCore.QRect(650, 224, 113, 27))
        self.lineEdit_y_min_3d.setObjectName(_fromUtf8("lineEdit_y_min_3d"))
        self.label_y_max_3d = QtGui.QLabel(self.tab_2)
        self.label_y_max_3d.setGeometry(QtCore.QRect(600, 259, 51, 17))
        self.label_y_max_3d.setObjectName(_fromUtf8("label_y_max_3d"))
        self.lineEdit_y_max_3d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_y_max_3d.setGeometry(QtCore.QRect(650, 253, 113, 27))
        self.lineEdit_y_max_3d.setObjectName(_fromUtf8("lineEdit_y_max_3d"))
        self.label_y_min_3d = QtGui.QLabel(self.tab_2)
        self.label_y_min_3d.setGeometry(QtCore.QRect(600, 229, 51, 17))
        self.label_y_min_3d.setObjectName(_fromUtf8("label_y_min_3d"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        RPlot.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RPlot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        RPlot.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(RPlot)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        RPlot.setStatusBar(self.statusBar)

        self.retranslateUi(RPlot)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(RPlot)

    def retranslateUi(self, RPlot):
        RPlot.setWindowTitle(_translate("RPlot", "MainWindow", None))
        self.label_x_max.setText(_translate("RPlot", "x_max:", None))
        self.label.setText(_translate("RPlot", "Expression:", None))
        self.Plot_cos.setText(_translate("RPlot", "Plot cos", None))
        self.label_x_min.setText(_translate("RPlot", "x_min:", None))
        self.Plot_2.setText(_translate("RPlot", "Plot x^2", None))
        self.label_pts.setText(_translate("RPlot", "no of pts:", None))
        self.Plot_sin.setText(_translate("RPlot", "Plot sin", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RPlot", "Tab 1", None))
        self.Plot_surface.setText(_translate("RPlot", "Plot surface", None))
        self.label_2.setText(_translate("RPlot", "Expression:", None))
        self.label_x_min_3d.setText(_translate("RPlot", "x_min:", None))
        self.label_pts_3d.setText(_translate("RPlot", "no of pts:", None))
        self.label_x_max_3d.setText(_translate("RPlot", "x_max:", None))
        self.label_y_max_3d.setText(_translate("RPlot", "y_max:", None))
        self.label_y_min_3d.setText(_translate("RPlot", "y_min:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RPlot", "Tab 2", None))

from pyqtgraph.opengl import GLViewWidget
from pyqtgraph import GraphicsLayoutWidget
