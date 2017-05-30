# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs\AboutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.setWindowModality(QtCore.Qt.WindowModal)
        aboutDialog.resize(289, 109)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutDialog.sizePolicy().hasHeightForWidth())
        aboutDialog.setSizePolicy(sizePolicy)
        aboutDialog.setMinimumSize(QtCore.QSize(0, 0))
        aboutDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        aboutDialog.setModal(True)
        self.label = QtWidgets.QLabel(aboutDialog)
        self.label.setGeometry(QtCore.QRect(9, 9, 255, 91))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "Apie"))
        self.label.setText(_translate("aboutDialog", "<html>\n"
"<body>\n"
"    <p>\n"
"        <span style=\"font-weight:600;\">Autorius</span>: Kulverstukas<br/>\n"
"        <span style=\" font-weight:600;\">Sukurta</span>: 2017.04.28<br/>\n"
"        <span style=\" font-weight:600;\">Svetainė</span>: <a href=\"http://9v.lt\">http://9v.lt</a><br/>\n"
"        <span style=\" font-weight:600;\">Aprašymas</span>:<br/>\n"
"        Programa kuri nurodytu laiku paleidžia garsinį signalą.<br/>\n"
"        Sukurta naudoti Duatlono sporte.<br/>\n"
"    </p>\n"
"</body>\n"
"</html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutDialog = QtWidgets.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())

