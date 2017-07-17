# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs\SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.setWindowModality(QtCore.Qt.WindowModal)
        settingsDialog.resize(360, 180)
        self.groupBox = QtWidgets.QGroupBox(settingsDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 211, 51))
        self.groupBox.setObjectName("groupBox")
        self.soundFilePath = QtWidgets.QLineEdit(self.groupBox)
        self.soundFilePath.setEnabled(True)
        self.soundFilePath.setGeometry(QtCore.QRect(50, 20, 151, 20))
        self.soundFilePath.setReadOnly(True)
        self.soundFilePath.setObjectName("soundFilePath")
        self.selectSoundFile = QtWidgets.QToolButton(self.groupBox)
        self.selectSoundFile.setGeometry(QtCore.QRect(20, 20, 25, 21))
        self.selectSoundFile.setObjectName("selectSoundFile")
        self.groupBox_2 = QtWidgets.QGroupBox(settingsDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 10, 121, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.preStartSecs = QtWidgets.QSpinBox(self.groupBox_2)
        self.preStartSecs.setGeometry(QtCore.QRect(20, 20, 51, 22))
        self.preStartSecs.setMinimum(3)
        self.preStartSecs.setProperty("value", 3)
        self.preStartSecs.setObjectName("preStartSecs")
        self.okBtn = QtWidgets.QPushButton(settingsDialog)
        self.okBtn.setGeometry(QtCore.QRect(10, 140, 75, 23))
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(settingsDialog)
        self.cancelBtn.setGeometry(QtCore.QRect(90, 140, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.groupBox_3 = QtWidgets.QGroupBox(settingsDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(230, 70, 121, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.bigClockSize = QtWidgets.QSpinBox(self.groupBox_3)
        self.bigClockSize.setGeometry(QtCore.QRect(20, 20, 51, 22))
        self.bigClockSize.setMinimum(0)
        self.bigClockSize.setMaximum(100)
        self.bigClockSize.setSingleStep(5)
        self.bigClockSize.setProperty("value", 0)
        self.bigClockSize.setObjectName("bigClockSize")

        self.retranslateUi(settingsDialog)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        _translate = QtCore.QCoreApplication.translate
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Nustatymai"))
        self.groupBox.setTitle(_translate("settingsDialog", "Garso failas"))
        self.selectSoundFile.setText(_translate("settingsDialog", "..."))
        self.groupBox_2.setTitle(_translate("settingsDialog", "Sekundės iki starto"))
        self.okBtn.setText(_translate("settingsDialog", "Gerai"))
        self.cancelBtn.setText(_translate("settingsDialog", "Atšaukti"))
        self.groupBox_3.setTitle(_translate("settingsDialog", "Didelio laimačio dydis"))
        self.bigClockSize.setSuffix(_translate("settingsDialog", " %"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settingsDialog = QtWidgets.QDialog()
    ui = Ui_settingsDialog()
    ui.setupUi(settingsDialog)
    settingsDialog.show()
    sys.exit(app.exec_())

