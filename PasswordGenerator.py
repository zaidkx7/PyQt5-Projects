from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        PasswordGenerator.setWindowIcon(QtGui.QIcon('BeginnerLevel/Icons/randomIcon.png'))
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(609, 399)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PasswordGenerator.sizePolicy().hasHeightForWidth())
        PasswordGenerator.setSizePolicy(sizePolicy)
        PasswordGenerator.setMinimumSize(QtCore.QSize(609, 399))
        PasswordGenerator.setMaximumSize(QtCore.QSize(609, 399))
        self.centralwidget = QtWidgets.QWidget(PasswordGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 100, 591, 251))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.optionsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.optionsLayout.setContentsMargins(0, 0, 0, 0)
        self.optionsLayout.setObjectName("optionsLayout")
        self.optionsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.optionsLabel.setObjectName("optionsLabel")
        self.optionsLayout.addWidget(self.optionsLabel)
        self.uppercaseCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.uppercaseCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uppercaseCheckBox.setObjectName("uppercaseCheckBox")
        self.optionsLayout.addWidget(self.uppercaseCheckBox)
        self.lowercaseCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.lowercaseCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lowercaseCheckBox.setObjectName("lowercaseCheckBox")
        self.optionsLayout.addWidget(self.lowercaseCheckBox)
        self.digitsCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.digitsCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitsCheckBox.setObjectName("digitsCheckBox")
        self.optionsLayout.addWidget(self.digitsCheckBox)
        self.symbolsCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.symbolsCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.symbolsCheckBox.setObjectName("symbolsCheckBox")
        self.optionsLayout.addWidget(self.symbolsCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.optionsLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.optionsLayout.addWidget(self.label_3)
        self.PasswordLength = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PasswordLength.setFont(font)
        self.PasswordLength.setAlignment(QtCore.Qt.AlignCenter)
        self.PasswordLength.setMinimum(5)
        self.PasswordLength.setMaximum(20)
        self.PasswordLength.setProperty("value", 10)
        self.PasswordLength.setObjectName("PasswordLength")
        self.optionsLayout.addWidget(self.PasswordLength)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.GenerateLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.GenerateLayout.setContentsMargins(0, 0, 0, 0)
        self.GenerateLayout.setObjectName("GenerateLayout")
        self.PasswordLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.GenerateLayout.addWidget(self.PasswordLabel, 1, 0, 1, 1)
        self.PasswordInput = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PasswordInput.sizePolicy().hasHeightForWidth())
        self.PasswordInput.setSizePolicy(sizePolicy)
        self.PasswordInput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PasswordInput.setReadOnly(True)
        self.PasswordInput.setBackgroundVisible(False)
        self.PasswordInput.setObjectName("PasswordInput")
        self.GenerateLayout.addWidget(self.PasswordInput, 1, 1, 1, 1)
        self.CopyButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.CopyButton.setFont(font)
        self.CopyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CopyButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BeginnerLevel/Icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CopyButton.setIcon(icon)
        self.CopyButton.setObjectName("CopyButton")
        self.GenerateLayout.addWidget(self.CopyButton, 1, 2, 1, 1)
        self.GenerateButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GenerateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GenerateButton.setObjectName("GenerateButton")
        self.GenerateLayout.addWidget(self.GenerateButton, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.GenerateLayout.addItem(spacerItem1, 0, 1, 1, 1)
        PasswordGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordGenerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 21))
        self.menubar.setObjectName("menubar")
        PasswordGenerator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PasswordGenerator)
        self.statusbar.setObjectName("statusbar")
        PasswordGenerator.setStatusBar(self.statusbar)

        """
        I prefer to use the dark theme, if you want to use the light theme,
        you can remove the dark theme styling by commenting out the below code 
        and use the light theme styling.
        """
        # Add dark theme styling
        PasswordGenerator.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QPlainTextEdit {
                background-color: #3b3b3b;
                border: 1px solid #555555;
                border-radius: 3px;
                padding: 2px;
            }
            QPushButton {
                background-color: #444444;
                border: 1px solid #555555;
                border-radius: 3px;
                padding: 5px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #4f4f4f;
            }
            QSpinBox {
                background-color: #3b3b3b;
                border: 1px solid #555555;
                border-radius: 3px;
                padding: 2px;
            }
            QCheckBox {
                spacing: 5px;
            }
            QCheckBox::indicator {
                width: 13px;
                height: 13px;
            }
        """)

        self.retranslateUi(PasswordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)

        
        self.GenerateButton.clicked.connect(self.generate_password)
        self.CopyButton.clicked.connect(self.copy_password)


    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator"))
        self.optionsLabel.setText(_translate("PasswordGenerator", "Password Options"))
        self.uppercaseCheckBox.setText(_translate("PasswordGenerator", "Use Uppercase Characters"))
        self.lowercaseCheckBox.setText(_translate("PasswordGenerator", "Use Lowercase Characters"))
        self.digitsCheckBox.setText(_translate("PasswordGenerator", "Use Digits"))
        self.symbolsCheckBox.setText(_translate("PasswordGenerator", "Use Symbols"))
        self.label_3.setText(_translate("PasswordGenerator", "Password Length"))
        self.PasswordLabel.setText(_translate("PasswordGenerator", "Password"))
        self.GenerateButton.setText(_translate("PasswordGenerator", "Generate"))

    def generate_password(self):
        if not any([self.uppercaseCheckBox.isChecked(), self.lowercaseCheckBox.isChecked(), 
                    self.digitsCheckBox.isChecked(), self.symbolsCheckBox.isChecked()]):
            self.PasswordInput.setStyleSheet('color: red; background-color: #3b3b3b;')
            self.PasswordInput.setPlainText('Please select at least one option')
            return
        
        self.PasswordInput.setStyleSheet('color: white; background-color: #3b3b3b;')
        password = ''
        length = self.PasswordLength.value() or 10

        char_pool = ''
        if self.uppercaseCheckBox.isChecked():
            uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            char_pool += uppercase_chars
            password += random.choice(uppercase_chars) 

        if self.lowercaseCheckBox.isChecked():
            lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
            char_pool += lowercase_chars
            password += random.choice(lowercase_chars)  

        if self.digitsCheckBox.isChecked():
            digits = '0123456789'
            char_pool += digits
            password += random.choice(digits) 

        if self.symbolsCheckBox.isChecked():
            symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
            char_pool += symbols
            password += random.choice(symbols)

        while len(password) < length:
            password += random.choice(char_pool)

        self.PasswordInput.setPlainText(password)

    def copy_password(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.PasswordInput.toPlainText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordGenerator = QtWidgets.QMainWindow()
    ui = Ui_PasswordGenerator()
    ui.setupUi(PasswordGenerator)
    PasswordGenerator.show()
    sys.exit(app.exec_())
