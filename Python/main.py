from object import Zonwering
import time
from Dashboard import Dashboard as db
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d1 = db.Dashboard()



    z1 = Zonwering()
    d1.addTab(1)
    d1.addTab(2)

    d1.show()

    time.sleep(2)
    d1.w1.setcurrentTemp(100)
    time.sleep(0.1)

    sys.exit(app.exec_())
