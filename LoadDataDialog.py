# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs\LoadDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fromMemoryDialog(object):
    def setupUi(self, fromMemoryDialog):
        fromMemoryDialog.setObjectName("fromMemoryDialog")
        fromMemoryDialog.setWindowModality(QtCore.Qt.WindowModal)
        fromMemoryDialog.resize(351, 318)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fromMemoryDialog.sizePolicy().hasHeightForWidth())
        fromMemoryDialog.setSizePolicy(sizePolicy)
        fromMemoryDialog.setMinimumSize(QtCore.QSize(0, 0))
        fromMemoryDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        fromMemoryDialog.setToolTip("")
        fromMemoryDialog.setSizeGripEnabled(False)
        fromMemoryDialog.setModal(True)
        self.okBtn = QtWidgets.QPushButton(fromMemoryDialog)
        self.okBtn.setGeometry(QtCore.QRect(240, 30, 75, 23))
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(fromMemoryDialog)
        self.cancelBtn.setGeometry(QtCore.QRect(240, 70, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.clearBtn = QtWidgets.QPushButton(fromMemoryDialog)
        self.clearBtn.setGeometry(QtCore.QRect(240, 110, 75, 23))
        self.clearBtn.setObjectName("clearBtn")
        self.dataText = QtWidgets.QPlainTextEdit(fromMemoryDialog)
        self.dataText.setGeometry(QtCore.QRect(20, 20, 201, 280))
        self.dataText.setObjectName("dataText")
        self.runnerDataFrame = QtWidgets.QFrame(fromMemoryDialog)
        self.runnerDataFrame.setGeometry(QtCore.QRect(10, 10, 221, 301))
        self.runnerDataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.runnerDataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.runnerDataFrame.setObjectName("runnerDataFrame")
        self.runnerNrDataText = QtWidgets.QPlainTextEdit(self.runnerDataFrame)
        self.runnerNrDataText.setGeometry(QtCore.QRect(10, 10, 101, 280))
        self.runnerNrDataText.setObjectName("runnerNrDataText")
        self.runnerTimeDataText = QtWidgets.QPlainTextEdit(self.runnerDataFrame)
        self.runnerTimeDataText.setGeometry(QtCore.QRect(110, 10, 101, 280))
        self.runnerTimeDataText.setObjectName("runnerTimeDataText")
        self.inputMethodToggle = QtWidgets.QCheckBox(fromMemoryDialog)
        self.inputMethodToggle.setGeometry(QtCore.QRect(240, 150, 101, 17))
        self.inputMethodToggle.setObjectName("inputMethodToggle")

        self.retranslateUi(fromMemoryDialog)
        QtCore.QMetaObject.connectSlotsByName(fromMemoryDialog)

    def retranslateUi(self, fromMemoryDialog):
        _translate = QtCore.QCoreApplication.translate
        fromMemoryDialog.setWindowTitle(_translate("fromMemoryDialog", "Įkelti duomenis"))
        self.okBtn.setText(_translate("fromMemoryDialog", "Gerai"))
        self.cancelBtn.setText(_translate("fromMemoryDialog", "Atšaukti"))
        self.clearBtn.setText(_translate("fromMemoryDialog", "Valyti"))
        self.dataText.setPlaceholderText(_translate("fromMemoryDialog", "Dalyvio nr. ir laikai"))
        self.runnerNrDataText.setPlaceholderText(_translate("fromMemoryDialog", "Dalyvio nr."))
        self.runnerTimeDataText.setPlaceholderText(_translate("fromMemoryDialog", "Laikai"))
        self.inputMethodToggle.setText(_translate("fromMemoryDialog", "Bendras įvedimas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fromMemoryDialog = QtWidgets.QDialog()
    ui = Ui_fromMemoryDialog()
    ui.setupUi(fromMemoryDialog)
    fromMemoryDialog.show()
    sys.exit(app.exec_())

