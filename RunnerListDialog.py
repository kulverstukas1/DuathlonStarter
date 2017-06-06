# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs\RunnerListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_runnerListDialog(object):
    def setupUi(self, runnerListDialog):
        runnerListDialog.setObjectName("runnerListDialog")
        runnerListDialog.setWindowModality(QtCore.Qt.NonModal)
        runnerListDialog.resize(340, 331)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(runnerListDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.runnerList = QtWidgets.QTableView(runnerListDialog)
        self.runnerList.setWordWrap(False)
        self.runnerList.setObjectName("runnerList")
        self.verticalLayout_2.addWidget(self.runnerList)

        self.retranslateUi(runnerListDialog)
        QtCore.QMetaObject.connectSlotsByName(runnerListDialog)

    def retranslateUi(self, runnerListDialog):
        _translate = QtCore.QCoreApplication.translate
        runnerListDialog.setWindowTitle(_translate("runnerListDialog", "Dalyvių sąrašas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    runnerListDialog = QtWidgets.QDialog()
    ui = Ui_runnerListDialog()
    ui.setupUi(runnerListDialog)
    runnerListDialog.show()
    sys.exit(app.exec_())

