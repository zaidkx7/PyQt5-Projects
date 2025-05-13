from PyQt5 import QtCore, QtGui, QtWidgets
import textblob
import googletrans
from PyQt5.QtWidgets import QMessageBox
import pyttsx3


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon("D:\\Qt5\\Icons\\fugue-icons-3.5.6\\icons\\application-ab.png"))
        MainWindow.resize(554, 288)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 201, 131))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"border:1px solid black;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 10, 201, 131))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"border:1px solid black;\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 12, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(71, 142, 213);\n"
"color:white;\n"
"border:1px solid black;\n"
"border-radius:20px\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgb(85, 0, 255);\n"
"color:white;\n"
"border:1px solid black;\n"
"border-radius:20px\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(71, 142, 213);\n"
"color:white;\n"
"border:1px solid black;\n"
"border-radius:20px\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgb(85, 0, 255);\n"
"color:white;\n"
"border:1px solid black;;\n"
"border-radius:20px\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 151, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setStyleSheet("QComboBox{\n"
"background-color:rgb(71, 142, 213);\n"
"color:white;\n"
"border:1px solid black;\n"
"border-radius:20px;\n"
"}\n"
"QComboBox::focus{\n"
"background-color:rgb(85, 0, 255);\n"
"color:white;\n"
"border:1px solid black;\n"
"border-radius:20px\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(340, 150, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox{\n"
"background-color:rgb(71, 142, 213);\n"
"color:white;\n"
"border:1px solid black;\n"
"border-radius:20px;\n"
"}\n"
"QComboBox::focus{\n"
"background-color:rgb(85, 0, 255);\n"
"color:white;\n"
"border:1px solid black;\n"
"border-radius:20px\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 209, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.translate)
        self.pushButton_2.clicked.connect(self.clear)

        self.languages = googletrans.LANGUAGES
        self.languages_list = list(self.languages.values())

        self.comboBox.addItems(self.languages_list)
        self.comboBox_2.addItems(self.languages_list)

        self.comboBox.setCurrentText("english")
        self.comboBox_2.setCurrentText("urdu")



    def translate(self):
        try:

            for key, value in self.languages.items():
                if (value == self.comboBox.currentText()):
                    from_language_key = key

            for key, value in self.languages.items():
                if (value == self.comboBox_2.currentText()):
                    to_language_key = key

            words = textblob.TextBlob(self.textEdit.toPlainText())
            words = words.translate(from_lang=from_language_key, to=to_language_key)
            self.textEdit_2.setText(str(words))
            engine = pyttsx3.init("espeak")

            engine.say(words)
            engine.runAndWait()

            self.label.setText(
                f'Translated from {self.comboBox.currentText()} to {self.comboBox_2.currentText()} language')



        except Exception as e:
            QMessageBox.about(self, "Translator", str(e))




    def clear(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")

        self.comboBox.setCurrentText("english")

        self.comboBox_2.setCurrentText("urdu")

        self.label.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Translator", "Translator"))
        self.pushButton.setText(_translate("MainWindow", "Translate"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
