#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from RPlot import Ui_RPlot
import pyqtgraph as pg

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui=Ui_RPlot()
        self.ui.setupUi(self)
        self.show()
                       
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
