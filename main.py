#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from RPlot import Ui_RPlot
import pyqtgraph as pg
import numpy as np
import pyqtgraph.opengl as gl

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
        
class Harshit(Ui_RPlot):
    def __init__(self):
        super(Harshit, self).__init__()

            
    def additional(self):
        # for 2d
        self.w = self.graphicsView.addPlot()
        #for 3d
        self.graphicsView_3d.show()
        self.graphicsView_3d.setWindowTitle('pyqtgraph example: GLSurfacePlot')
        self.graphicsView_3d.setCameraPosition(distance=50)
        g = gl.GLGridItem()
        g.scale(2,2,1)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        self.graphicsView_3d.addItem(g)
        self.graphicsView_3d.setGeometry(QtCore.QRect(2, 6, 581, 501))
        self.graphicsView_3d.setObjectName(_fromUtf8("graphicsView_3d"))
        QtCore.QObject.connect(self.Plot_sin, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sin_pressed)
        QtCore.QObject.connect(self.Plot_cos, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cos_pressed)
        QtCore.QObject.connect(self.Plot_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.square_pressed)
        QtCore.QObject.connect(self.Plot_surface, QtCore.SIGNAL(_fromUtf8("clicked()")), self.surface_pressed)
                
    def get_values(self):
        try:
            x_min = float(self.lineEdit_x_min.text())
            x_max = float(self.lineEdit_x_max.text())
            no_of_pts = int(self.lineEdit_pts.text())
            return (x_min, x_max, no_of_pts)
        except ValueError:
            print "One of the params is not in the desired format"
    def get_values_3d(self):
        try:
            x_min = float(self.lineEdit_x_min_3d.text())
            x_max = float(self.lineEdit_x_max_3d.text())
            y_min = float(self.lineEdit_y_min_3d.text())
            y_max = float(self.lineEdit_y_max_3d.text())
            no_of_pts = int(self.lineEdit_pts_3d.text())
            return (x_min, x_max, y_min, y_max, no_of_pts)
        except ValueError:
            print "One of the params is not in the desired format in 3d"
    def sin_pressed(self):
        x_min, x_max, no_of_points = self.get_values()
        x2 = np.linspace(x_min, x_max, no_of_points)
        data2 = np.sin(x2)
        self.w.plot(x2, data2, pen=(255,255,255,200))
    def cos_pressed(self):
        x_min, x_max, no_of_points = self.get_values()
        x2 = np.linspace(x_min, x_max, no_of_points)
        data2 = np.cos(x2)
        self.w.plot(x2, data2, pen=(255,0,0,200))
    def square_pressed(self):
        x_min, x_max, no_of_points = self.get_values()
        x2 = np.linspace(x_min, x_max, no_of_points)
        data2 = x2 ** 2
        self.w.plot(x2, data2, pen=(0,255,0,200))
    def surface_pressed(self):
        x_min, x_max, y_min, y_max, no_of_points = self.get_values_3d()
        x = np.linspace(x_min, x_max, no_of_points)
        y = np.linspace(y_min, y_max, no_of_points)
        z = 0.1 * ((x.reshape(no_of_points,1) ** 2) - (y.reshape(1,no_of_points) ** 2))
        p2 = gl.GLSurfacePlotItem(x=x, y=y, z=z, shader='normalColor')
        self.graphicsView_3d.addItem(p2)

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui=Harshit()
        self.ui.setupUi(self)
        self.ui.additional()
        self.show()
                       
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
