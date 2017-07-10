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
        bigClockDialog.resize(632, 349)
        bigClockDialog.setModal(False)
        self.currRunnerBox = QtWidgets.QGroupBox(bigClockDialog)
        self.currRunnerBox.setGeometry(QtCore.QRect(30, 190, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.currRunnerBox.setFont(font)
        self.currRunnerBox.setAlignment(QtCore.Qt.AlignCenter)
        self.currRunnerBox.setFlat(False)
        self.currRunnerBox.setCheckable(False)
        self.currRunnerBox.setObjectName("currRunnerBox")
        self.currRunnerLabel = QtWidgets.QLabel(self.currRunnerBox)
        self.currRunnerLabel.setGeometry(QtCore.QRect(10, 50, 231, 51))
        self.currRunnerLabel.setObjectName("currRunnerLabel")
        self.nextRunnerBox = QtWidgets.QGroupBox(bigClockDialog)
        self.nextRunnerBox.setGeometry(QtCore.QRect(350, 190, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.nextRunnerBox.setFont(font)
        self.nextRunnerBox.setAlignment(QtCore.Qt.AlignCenter)
        self.nextRunnerBox.setFlat(False)
        self.nextRunnerBox.setCheckable(False)
        self.nextRunnerBox.setObjectName("nextRunnerBox")
        self.nextRunnerLabel = QtWidgets.QLabel(self.nextRunnerBox)
        self.nextRunnerLabel.setGeometry(QtCore.QRect(10, 50, 231, 51))
        self.nextRunnerLabel.setObjectName("nextRunnerLabel")
        self.timerLabel = QtWidgets.QLabel(bigClockDialog)
        self.timerLabel.setGeometry(QtCore.QRect(40, 20, 551, 151))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.timerLabel.setFont(font)
        self.timerLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.timerLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.timerLabel.setLineWidth(1)
        self.timerLabel.setTextFormat(QtCore.Qt.PlainText)
        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.timerLabel.setObjectName("timerLabel")

        self.retranslateUi(bigClockDialog)
        QtCore.QMetaObject.connectSlotsByName(bigClockDialog)

    def retranslateUi(self, bigClockDialog):
        _translate = QtCore.QCoreApplication.translate
        bigClockDialog.setWindowTitle(_translate("bigClockDialog", "Didelis laikmatis"))
        self.currRunnerBox.setTitle(_translate("bigClockDialog", "Išbėgo"))
        self.currRunnerLabel.setText(_translate("bigClockDialog", "TextLabel"))
        self.nextRunnerBox.setTitle(_translate("bigClockDialog", "Ruošiasi"))
        self.nextRunnerLabel.setText(_translate("bigClockDialog", "TextLabel"))
        self.timerLabel.setText(_translate("bigClockDialog", "00:00,0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bigClockDialog = QtWidgets.QDialog()
    ui = Ui_bigClockDialog()
    ui.setupUi(bigClockDialog)
    bigClockDialog.show()
    sys.exit(app.exec_())

