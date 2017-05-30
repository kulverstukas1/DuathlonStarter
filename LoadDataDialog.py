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
        fromMemoryDialog.resize(333, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fromMemoryDialog.sizePolicy().hasHeightForWidth())
        fromMemoryDialog.setSizePolicy(sizePolicy)
        fromMemoryDialog.setMinimumSize(QtCore.QSize(0, 0))
        fromMemoryDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        fromMemoryDialog.setSizeGripEnabled(False)
        fromMemoryDialog.setModal(True)
        self.okBtn = QtWidgets.QPushButton(fromMemoryDialog)
        self.okBtn.setGeometry(QtCore.QRect(230, 20, 75, 23))
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(fromMemoryDialog)
        self.cancelBtn.setGeometry(QtCore.QRect(230, 60, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.clearBtn = QtWidgets.QPushButton(fromMemoryDialog)
        self.clearBtn.setGeometry(QtCore.QRect(230, 100, 75, 23))
        self.clearBtn.setObjectName("clearBtn")
        self.dataText = QtWidgets.QPlainTextEdit(fromMemoryDialog)
        self.dataText.setGeometry(QtCore.QRect(10, 10, 191, 281))
        self.dataText.setObjectName("dataText")

        self.retranslateUi(fromMemoryDialog)
        QtCore.QMetaObject.connectSlotsByName(fromMemoryDialog)

    def retranslateUi(self, fromMemoryDialog):
        _translate = QtCore.QCoreApplication.translate
        fromMemoryDialog.setWindowTitle(_translate("fromMemoryDialog", "Įkelti duomenis"))
        self.okBtn.setText(_translate("fromMemoryDialog", "Gerai"))
        self.cancelBtn.setText(_translate("fromMemoryDialog", "Atšaukti"))
        self.clearBtn.setText(_translate("fromMemoryDialog", "Valyti"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fromMemoryDialog = QtWidgets.QDialog()
    ui = Ui_fromMemoryDialog()
    ui.setupUi(fromMemoryDialog)
    fromMemoryDialog.show()
    sys.exit(app.exec_())

