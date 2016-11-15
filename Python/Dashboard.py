# importing moduless
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Main import Main
from Tab import Tab

# from object import *


class Dashboard(QWidget):


    def __init__(self):
        QWidget.__init__(self)
        self.devices = {}

        self.mainserial = Main()
        self.mainserial.addtab.connect(self.addTab)
        self.mainserial.deltab.connect(self.deleteTab)

        self.mainserial.start()
        self.drawDashboard(self)

    # Drawing the main widget with tab layout from multiple Tab Class
    # instances.
    def drawDashboard(self, Widget):
        # Create main widget.
        Widget.setObjectName("Widget")
        Widget.resize(612, 513)
        # Chosing the Window Title
        Widget.setWindowTitle("Dashboard Zeng Ltd.")
        # Using horizontal tab-layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Widget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Widget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    # Function to add a tab. This function takes a number from 1-4 as
    # parameter representing the number of the arduino
    def addTab(self, serialn, name):   #
        newtab = Tab()
        index = self.tabWidget.addTab(newtab.SunScreen1, name)
        self.devices[serialn] = {'name': name, 'tab': newtab, 'tabindex': index}
        print(self.devices)
    # Function to delete tab. This function takes a number from 1-4 as
    # parameter representing the number of the arduino

    def deleteTab(self, serialn):
        self.tabWidget.removeTab(self.devices[serialn]['tabindex'])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dash = Dashboard()
    dash.show()
    sys.exit(app.exec_())
