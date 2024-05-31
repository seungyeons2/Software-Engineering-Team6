# Form implementation generated from reading ui file 'level_select_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LevelSelect(object):
    def setupUi(self, LevelSelect):
        LevelSelect.setObjectName("LevelSelect")
        LevelSelect.resize(1000, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=LevelSelect)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 240, 991, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.easyButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.easyButton.setMinimumSize(QtCore.QSize(300, 70))
        self.easyButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.easyButton.setFont(font)
        self.easyButton.setObjectName("easyButton")
        self.horizontalLayout.addWidget(self.easyButton)
        self.normalButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.normalButton.setMinimumSize(QtCore.QSize(300, 70))
        self.normalButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.normalButton.setFont(font)
        self.normalButton.setObjectName("normalButton")
        self.horizontalLayout.addWidget(self.normalButton)
        self.hardButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.hardButton.setMinimumSize(QtCore.QSize(300, 70))
        self.hardButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hardButton.setFont(font)
        self.hardButton.setObjectName("hardButton")
        self.horizontalLayout.addWidget(self.hardButton)
        self.label = QtWidgets.QLabel(parent=LevelSelect)
        self.label.setGeometry(QtCore.QRect(304, 167, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(LevelSelect)
        QtCore.QMetaObject.connectSlotsByName(LevelSelect)

    def retranslateUi(self, LevelSelect):
        _translate = QtCore.QCoreApplication.translate
        LevelSelect.setWindowTitle(_translate("LevelSelect", "Dialog"))
        self.easyButton.setText(_translate("LevelSelect", "Easy"))
        self.normalButton.setText(_translate("LevelSelect", "Normal"))
        self.hardButton.setText(_translate("LevelSelect", "Hard"))
        self.label.setText(_translate("LevelSelect", "난이도를 선택하세요"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LevelSelect = QtWidgets.QDialog()
    ui = Ui_LevelSelect()
    ui.setupUi(LevelSelect)
    LevelSelect.show()
    sys.exit(app.exec())
