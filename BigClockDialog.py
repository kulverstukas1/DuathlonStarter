# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs\BigClockDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bigClockDialog(object):
    def setupUi(self, bigClockDialog):
        bigClockDialog.setObjectName("bigClockDialog")
        bigClockDialog.setWindowModality(QtCore.Qt.NonModal)
        bigClockDialog.resize(730, 430)
        bigClockDialog.setMinimumSize(QtCore.QSize(730, 430))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(bigClockDialog)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.timerLabel = QtWidgets.QLabel(bigClockDialog)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(120)
        font.setBold(True)
        font.setWeight(75)
        self.timerLabel.setFont(font)
        self.timerLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.timerLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.timerLabel.setLineWidth(1)
        self.timerLabel.setTextFormat(QtCore.Qt.PlainText)
        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.timerLabel.setObjectName("timerLabel")
        self.verticalLayout_2.addWidget(self.timerLabel)
        self.frame = QtWidgets.QFrame(bigClockDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currRunnerBox = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.currRunnerBox.setFont(font)
        self.currRunnerBox.setAlignment(QtCore.Qt.AlignCenter)
        self.currRunnerBox.setFlat(False)
        self.currRunnerBox.setCheckable(False)
        self.currRunnerBox.setObjectName("currRunnerBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.currRunnerBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.currRunnerLabel = QtWidgets.QLabel(self.currRunnerBox)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.currRunnerLabel.setFont(font)
        self.currRunnerLabel.setObjectName("currRunnerLabel")
        self.gridLayout_2.addWidget(self.currRunnerLabel, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.currRunnerBox)
        self.nextRunnerBox = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.nextRunnerBox.setFont(font)
        self.nextRunnerBox.setAutoFillBackground(False)
        self.nextRunnerBox.setAlignment(QtCore.Qt.AlignCenter)
        self.nextRunnerBox.setFlat(False)
        self.nextRunnerBox.setCheckable(False)
        self.nextRunnerBox.setObjectName("nextRunnerBox")
        self.gridLayout = QtWidgets.QGridLayout(self.nextRunnerBox)
        self.gridLayout.setObjectName("gridLayout")
        self.nextRunnerLabel = QtWidgets.QLabel(self.nextRunnerBox)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.nextRunnerLabel.setFont(font)
        self.nextRunnerLabel.setObjectName("nextRunnerLabel")
        self.gridLayout.addWidget(self.nextRunnerLabel, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.nextRunnerBox)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(bigClockDialog)
        QtCore.QMetaObject.connectSlotsByName(bigClockDialog)

    def retranslateUi(self, bigClockDialog):
        _translate = QtCore.QCoreApplication.translate
        bigClockDialog.setWindowTitle(_translate("bigClockDialog", "Didelis laikmatis"))
        self.timerLabel.setText(_translate("bigClockDialog", "00:00,0"))
        self.currRunnerBox.setTitle(_translate("bigClockDialog", "Išbėgo"))
        self.currRunnerLabel.setText(_translate("bigClockDialog", "TextLabel"))
        self.nextRunnerBox.setTitle(_translate("bigClockDialog", "Ruošiasi"))
        self.nextRunnerLabel.setText(_translate("bigClockDialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bigClockDialog = QtWidgets.QDialog()
    ui = Ui_bigClockDialog()
    ui.setupUi(bigClockDialog)
    bigClockDialog.show()
    sys.exit(app.exec_())

