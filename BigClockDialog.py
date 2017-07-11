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
        bigClockDialog.resize(640, 330)
        bigClockDialog.setMinimumSize(QtCore.QSize(640, 330))
        bigClockDialog.setAutoFillBackground(False)
        bigClockDialog.setModal(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(bigClockDialog)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.timerLabel = QtWidgets.QLabel(bigClockDialog)
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
        self.verticalLayout_2.addWidget(self.timerLabel)
        self.frame = QtWidgets.QFrame(bigClockDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currRunnerBox = QtWidgets.QGroupBox(self.frame)
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
        self.horizontalLayout.addWidget(self.currRunnerBox)
        self.nextRunnerBox = QtWidgets.QGroupBox(self.frame)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextRunnerLabel.sizePolicy().hasHeightForWidth())
        self.nextRunnerLabel.setSizePolicy(sizePolicy)
        self.nextRunnerLabel.setAutoFillBackground(False)
        self.nextRunnerLabel.setScaledContents(True)
        self.nextRunnerLabel.setObjectName("nextRunnerLabel")
        self.nextRunnerLabel.raise_()
        self.currRunnerBox.raise_()
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

