
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon('Calculator.png'))
        Dialog.resize(361, 588)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.outputlabel = QtWidgets.QLabel(Dialog)
        self.outputlabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.outputlabel.setFont(font)
        self.outputlabel.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.outputlabel.setMouseTracking(False)
        self.outputlabel.setStyleSheet("background-color: rgb(185, 157, 255);\n"
"color:white;")
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputlabel.setLineWidth(2)
        self.outputlabel.setMidLineWidth(0)
        self.outputlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputlabel.setObjectName("outputlabel")
        self.percentButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.percentButton.setObjectName("percentButton")
        self.CButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("C"))
        self.CButton.setGeometry(QtCore.QRect(100, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.CButton.setFont(font)
        self.CButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.CButton.setObjectName("CButton")
        self.arrowButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 120, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.divideButton.setObjectName("divideButton")
        self.eightButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.eightButton.setObjectName("eightButton")
        self.multiplyButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.multiplyButton.setObjectName("multiplyButton")
        self.sevenButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.sevenButton.setObjectName("sevenButton")
        self.nineButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 210, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.nineButton.setObjectName("nineButton")
        self.fiveButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 300, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.fiveButton.setObjectName("fiveButton")
        self.minusButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 300, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.minusButton.setObjectName("minusButton")
        self.fourButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 300, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.fourButton.setObjectName("fourButton")
        self.sixButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 300, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.sixButton.setObjectName("sixButton")
        self.twoButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 390, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.twoButton.setObjectName("twoButton")
        self.plusButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(275, 390, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusButton.setFont(font)
        self.plusButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.plusButton.setObjectName("plusButton")
        self.oneButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 390, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.oneButton.setObjectName("oneButton")
        self.threeButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 390, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.threeButton.setObjectName("threeButton")
        self.zeroButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.zeroButton.setObjectName("zeroButton")
        self.equalButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.eval_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.equalButton.setObjectName("equalButton")
        self.plusminusButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.plusminusButton.setObjectName("plusminusButton")
        self.decimalButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setStyleSheet("QPushButton{color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(185, 157, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:red;\n"
"}")
        self.decimalButton.setObjectName("decimalButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def eval_it(self):
        try:
            screen = self.outputlabel.text()
            answer = eval(screen)
            self.outputlabel.setText(str(answer))
        except:
            self.outputlabel.setText("Syntax Error")

    def plus_minus_it(self):
        screen = self.outputlabel.text()
        if "-" in screen:
            self.outputlabel.setText(screen.replace("-",""))
        else:
            self.outputlabel.setText(f'-{screen}')


    def remove_it(self):
        screen = self.outputlabel.text()
        screen = screen[:-1]

        self.outputlabel.setText(f'{screen}')

    def dot_it(self):
        screen = self.outputlabel.text()
        if "." in screen:
            pass
        else:
            self.outputlabel.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.outputlabel.setText("0")
        else:
            if self.outputlabel.text() == "0":
                self.outputlabel.setText("")
            self.outputlabel.setText(f'{self.outputlabel.text()}{pressed}')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.outputlabel.setText(_translate("Dialog", "0"))
        self.percentButton.setText(_translate("Dialog", "%"))
        self.CButton.setText(_translate("Dialog", "C"))
        self.arrowButton.setText(_translate("Dialog", "<<"))
        self.divideButton.setText(_translate("Dialog", "/"))
        self.eightButton.setText(_translate("Dialog", "8"))
        self.multiplyButton.setText(_translate("Dialog", "x"))
        self.sevenButton.setText(_translate("Dialog", "7"))
        self.nineButton.setText(_translate("Dialog", "9"))
        self.fiveButton.setText(_translate("Dialog", "5"))
        self.minusButton.setText(_translate("Dialog", "-"))
        self.fourButton.setText(_translate("Dialog", "4"))
        self.sixButton.setText(_translate("Dialog", "6"))
        self.twoButton.setText(_translate("Dialog", "2"))
        self.plusButton.setText(_translate("Dialog", "+"))
        self.oneButton.setText(_translate("Dialog", "1"))
        self.threeButton.setText(_translate("Dialog", "3"))
        self.zeroButton.setText(_translate("Dialog", "0"))
        self.equalButton.setText(_translate("Dialog", "="))
        self.plusminusButton.setText(_translate("Dialog", "+/-"))
        self.decimalButton.setText(_translate("Dialog", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
