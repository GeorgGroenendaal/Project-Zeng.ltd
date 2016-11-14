from object import Zonwering
from object import ToGUI
import time
from Dashboard import Dashboard
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d1 = Dashboard()
    d1.show()

    d1.addTab(1)
    d1.addTab(2)
    d1.addTab(3)
    d1.addTab(4)

    z1 = Zonwering()
    tg = ToGUI()
    time.sleep(2)
    z1.get_current_temp()
    d1.w1.setcurrentTemp(tg.return_current_temp)
    time.sleep(0.1)

    sys.exit(app.exec_())
