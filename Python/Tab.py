from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Tab(QWidget):  # Class Tab, holding all the layout and design choices.

    def __init__(self):
        QWidget.__init__(self)
        self.makeTab(self)

    def makeTab(self, Widget):  # Function to create User Interface.
        # First Tab.

        self.setGeometry(QtCore.QRect(612, 513, 0, 0))
        self.SunScreen1 = QtWidgets.QWidget()
        self.SunScreen1.setObjectName("SunScreen1")

        # Drawing vertical and horizontal lines on the GUI.
        self.verticalLine1 = QtWidgets.QFrame(self.SunScreen1)
        self.verticalLine1.setGeometry(QtCore.QRect(0, 91, 591, 20))
        self.verticalLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.verticalLine1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLine1.setObjectName("verticalLine1")
        self.horizontalLine = QtWidgets.QFrame(self.SunScreen1)
        self.horizontalLine.setGeometry(QtCore.QRect(280, 100, 20, 371))
        self.horizontalLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.horizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLine.setObjectName("horizontalLine")
        self.verticalLine2 = QtWidgets.QFrame(self.SunScreen1)
        self.verticalLine2.setGeometry(QtCore.QRect(0, 183, 581, 20))
        self.verticalLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.verticalLine2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLine2.setObjectName("verticalLine2")
        self.verticalLine3 = QtWidgets.QFrame(self.SunScreen1)
        self.verticalLine3.setGeometry(QtCore.QRect(0, 320, 581, 20))
        self.verticalLine3.setFrameShape(QtWidgets.QFrame.HLine)
        self.verticalLine3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLine3.setObjectName("verticalLine3")

        # Current statistics:
        # Setting font
        font = QtGui.QFont()
        font.setPointSize(19)
        # Current Temperature
        self.currentTemp = QtWidgets.QLabel(self.SunScreen1)
        self.currentTemp.setGeometry(QtCore.QRect(70, 51, 81, 23))
        self.currentTemp.setFont(font)
        self.currentTemp.setText("Unknown")
        self.currentTemp_lbl = QtWidgets.QLabel(self.SunScreen1)
        self.currentTemp.setObjectName("currentTemp")
        self.currentTemp_lbl.setText("Current Temperature:")
        self.currentTemp_lbl.setObjectName("currentTemp_lbl")
        # Current Light Intensity
        self.currentLight = QtWidgets.QLabel(self.SunScreen1)
        self.currentLight.setGeometry(QtCore.QRect(275, 51, 81, 23))
        self.currentLight.setFont(font)
        self.currentLight.setText("Unknown")
        self.currentLight.setObjectName("currentLight")
        self.currentLight_lbl = QtWidgets.QLabel(self.SunScreen1)
        self.currentLight_lbl.setGeometry(QtCore.QRect(220, 12, 140, 16))
        self.currentLight_lbl.setText("Current Light Intensity:")
        self.currentLight_lbl.setObjectName("currentLight_lbl")
        # Current Roll - Out
        self.currentRoll = QtWidgets.QLabel(self.SunScreen1)
        self.currentRoll.setGeometry(QtCore.QRect(485, 51, 81, 23))
        self.currentRoll.setFont(font)
        self.currentRoll.setText("Unknown")
        self.currentRoll.setObjectName("currentRoll")
        self.currentRoll_lbl = QtWidgets.QLabel(self.SunScreen1)
        self.currentRoll_lbl.setGeometry(QtCore.QRect(444, 12, 118, 16))
        self.currentRoll_lbl.setText("Current Roll-Out:")
        self.currentRoll_lbl.setObjectName("currentRoll_lbl")
        self.currentTemp_lbl.setGeometry(QtCore.QRect(20, 12, 132, 16))

        # First 'container' on left side : temperature sensor settings
        # Label
        self.tempSens_lbl = QtWidgets.QLabel(self.SunScreen1)
        self.tempSens_lbl.setGeometry(QtCore.QRect(10, 110, 123, 16))
        self.tempSens_lbl.setText("Temperature sensor")
        self.tempSens_lbl.setObjectName("tempSens_lbl")
        # Text Line Edit
        self.tempSens_line = QtWidgets.QLineEdit(self.SunScreen1)
        self.tempSens_line.setGeometry(QtCore.QRect(10, 140, 161, 31))
        self.tempSens_line.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tempSens_line.setText("")
        self.tempSens_line.setMaxLength(2)
        self.tempSens_line.setPlaceholderText("Temperature in Cº")
        self.tempSens_line.setObjectName("tempSens_line")
        # Apply button
        self.tempSens_btn = QtWidgets.QPushButton(self.SunScreen1)
        self.tempSens_btn.setGeometry(QtCore.QRect(200, 140, 61, 32))
        self.tempSens_btn.setText("Apply")
        self.tempSens_btn.setObjectName("tempSens_btn")
        # Link apply button to function
        self.tempSens_btn.clicked.connect(self.buttonclicktempSens)

        # Second 'container' on left side : light intensity sensor settings
        # Label
        self.lightSens_lbl = QtWidgets.QLabel(self.SunScreen1)
        self.lightSens_lbl.setGeometry(QtCore.QRect(10, 200, 130, 16))
        self.lightSens_lbl.setFocusPolicy(QtCore.Qt.TabFocus)
        self.lightSens_lbl.setText("Light intensity sensor")
        self.lightSens_lbl.setObjectName("lightSens_lbl")
        # Dropdown menu
        self.lightintsens_dropdown = QtWidgets.QComboBox(self.SunScreen1)
        self.lightintsens_dropdown.setGeometry(QtCore.QRect(10, 240, 161, 51))
        self.lightintsens_dropdown.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lightintsens_dropdown.setContextMenuPolicy(
            QtCore.Qt.DefaultContextMenu)
        self.lightintsens_dropdown.setObjectName("lightintsens_dropdown")
        self.lightintsens_dropdown.addItem("")
        self.lightintsens_dropdown.setItemText(0, "Cloudy")
        self.lightintsens_dropdown.addItem("")
        self.lightintsens_dropdown.setItemText(1, "Partly Cloudy")
        self.lightintsens_dropdown.addItem("")
        self.lightintsens_dropdown.setItemText(2, "Sunny")
        self.lightintsens_dropdown.addItem("")
        self.lightintsens_dropdown.setItemText(3, "Bright")
        # Apply Button
        self.lightSens_btn = QtWidgets.QPushButton(self.SunScreen1)
        self.lightSens_btn.setGeometry(QtCore.QRect(200, 250, 61, 32))
        self.lightSens_btn.setText("Apply")
        self.lightSens_btn.setObjectName("lightSens_btn")
        # Link button to function
        self.lightSens_btn.clicked.connect(self.buttonclicklightSens)

        # Third 'container' on the left side: settings
        # Label
        self.settings_lbl = QtWidgets.QLabel(self.SunScreen1)
        self.settings_lbl.setGeometry(QtCore.QRect(10, 340, 50, 16))
        self.settings_lbl.setText("Settings")
        self.settings_lbl.setObjectName("settings_lbl")
        # Text Line Edit
        self.maxIn_line = QtWidgets.QLineEdit(self.SunScreen1)
        self.maxIn_line.setGeometry(QtCore.QRect(10, 370, 161, 31))
        self.maxIn_line.setText("")
        self.maxIn_line.setMaxLength(3)
        self.maxIn_line.setPlaceholderText("Max Roll-In in CM")
        self.maxIn_line.setObjectName("maxIn_line")
        self.maxOut_line = QtWidgets.QLineEdit(self.SunScreen1)
        self.maxOut_line.setGeometry(QtCore.QRect(10, 410, 161, 31))
        self.maxOut_line.setText("")
        self.maxOut_line.setMaxLength(3)
        self.maxOut_line.setPlaceholderText("Max Roll-Out in CM")
        self.maxOut_line.setObjectName("maxOut_line")
        # Apply button
        self.setting_btn = QtWidgets.QPushButton(self.SunScreen1)
        self.setting_btn.setGeometry(QtCore.QRect(200, 390, 61, 32))
        self.setting_btn.setText("Apply")
        self.setting_btn.setObjectName("setting_btn")
        # Link apply button to function
        self.setting_btn.clicked.connect(self.buttonclickSettings)

        # First 'container' on the right side: Manual Use
        # Label
        self.manualUse_lbl = QtWidgets.QLabel(self.SunScreen1)
        self.manualUse_lbl.setGeometry(QtCore.QRect(300, 110, 71, 16))
        self.manualUse_lbl.setText("Manual Use")
        self.manualUse_lbl.setObjectName("manualUse_lbl")
        # In Button
        self.in_btn = QtWidgets.QPushButton(self.SunScreen1)
        self.in_btn.setGeometry(QtCore.QRect(300, 130, 131, 51))
        self.in_btn.setText("In")
        self.in_btn.setObjectName("in_btn")
        # Link apply in-button to function
        # self.in_btn.clicked.connect(self.manualIn)
        # Out Button
        self.out_btn = QtWidgets.QPushButton(self.SunScreen1)
        self.out_btn.setGeometry(QtCore.QRect(430, 130, 131, 51))
        self.out_btn.setText("Out")
        self.out_btn.setObjectName("out_btn")
        # Link out-button to function
        # self.out_btn.clicked.connect(self.manualOut)
        # Link in-button to function
        # self.in_btn.clicked.connect(self.manualIn)

        # Second 'container' on the right side: Use History Graph
        # Label
        self.useHistory_lbl = QtWidgets.QLabel(self.SunScreen1)
        self.useHistory_lbl.setGeometry(QtCore.QRect(300, 200, 150, 20))
        self.useHistory_lbl.setText("Use Statistics")
        self.useHistory_lbl.setObjectName("useHistory_lbl")
        # Buttons for graph
        self.usegraph_btn = QtWidgets.QPushButton(self.SunScreen1)
        self.usegraph_btn.setGeometry(QtCore.QRect(430, 240, 131, 51))
        self.usegraph_btn.setText("Graph")
        self.usegraph_btn.setObjectName("useGraphbtn")
        self.usebar_btn = QtWidgets.QPushButton(self.SunScreen1)
        self.usebar_btn.setGeometry(QtCore.QRect(300, 240, 131, 51))
        self.usebar_btn.setText("Bar")
        self.usebar_btn.setObjectName("useBarbtn")
        # Linking buttons to function
        self.usegraph_btn.clicked.connect(self.openuseGraph)
        self.usebar_btn.clicked.connect(self.openuseBar)

        # Third 'container' on the right side : Temperature History Graph
        # Label
        self.tempHistory_lbl = QtWidgets.QLabel(self.SunScreen1)
        self.tempHistory_lbl.setGeometry(QtCore.QRect(300, 340, 150, 20))
        self.tempHistory_lbl.setText("Temperature Statistics")
        self.tempHistory_lbl.setObjectName("tempHistory_lbl")
        # Graph and Bar Chart Buttons.
        self.tempgraph_btn = QtWidgets.QPushButton(self.SunScreen1)
        self.tempgraph_btn.setGeometry(QtCore.QRect(430, 380, 131, 51))
        self.tempgraph_btn.setText("Graph")
        self.tempgraph_btn.setObjectName("tempGraphbtn")
        self.tempbar_btn = QtWidgets.QPushButton(self.SunScreen1)
        self.tempbar_btn.setGeometry(QtCore.QRect(300, 380, 131, 51))
        self.tempbar_btn.setText("Bar")
        self.tempbar_btn.setObjectName("tempBarbtn")
        # Link buttons to function
        self.tempgraph_btn.clicked.connect(self.opentempGraph)
        self.tempbar_btn.clicked.connect(self.opentempBar)

    # Open window with use history bar chart TODO

    def openuseBar(self):
        pass

    # Open window with use history graph TODO
    def openuseGraph(self):
        pass

    # Open window with temperature bar chart TODO
    def opentempBar(self):
        pass

    # Open tab with temperature graph TODO
    def opentempGraph(self):
        pass

    def setcurrentTemp(self, temp):  # Function to set current temperature
        self.currentTemp.setText("{0} Cº".format(int(temp)))

    def setcurrentLight(self, light):   # Function to set current light.
        self.currentLight.setText("{0} %".format(str(light)))

    def setcurrentRoll(self, roll):  # Function to set current roll-out
        self.currentRoll.setText("{0} %".format(str(roll)))

    def buttonclicktempSens(self):  # Function to get temp sens line.
        temp = self.tempSens_line.text()
        return int(temp)

    def buttonclickSettings(self):  # Function to get maxin and maxout line.
        maxIn = self.maxIn_line.text()
        maxOut = self.maxOut_line.text()
        return int(maxIn), int(maxOut)

    def buttonclicklightSens(self):  # Function to get current dropdown text.
        value = self.lightintsens_dropdown.currentText()
        if value == "Cloudy":
            return 15   # Light percentage
        elif value == "Partly Cloudy":
            return 25  # Light percentage
        elif value == "Sunny":
            return 50  # Light percentage
        else:
            return 70  # Light percentage

    # # Use Henk's manual in function TODO
    # def manualIn(self):
    #     Zonwering.manual_rollup()
    #
    # # Use Henk's manual out function TODO
    # def manualOut(self):
    #     Zonwering.manual_rolldown()
