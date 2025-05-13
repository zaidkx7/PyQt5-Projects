from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TicTacToe(object):
    def setupUi(self, TicTacToe):
        TicTacToe.setObjectName("TicTacToe")
        TicTacToe.setWindowIcon(QtGui.QIcon('BeginnerLevel/Icons/game.png'))
        TicTacToe.resize(609, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TicTacToe.sizePolicy().hasHeightForWidth())
        TicTacToe.setSizePolicy(sizePolicy)
        TicTacToe.setMinimumSize(QtCore.QSize(609, 370))
        TicTacToe.setMaximumSize(QtCore.QSize(609, 370))
        TicTacToe.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                background-color: #3b3b3b;
                color: #ffffff;
                border: 2px solid #555555;
                border-radius: 5px;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #454545;
                border: 2px solid #666666;
            }
            QPushButton:pressed {
                background-color: #2b2b2b;
            }
            QPushButton:disabled {
                background-color: #2b2b2b;
                border: 2px solid #333333;
                color: #666666;
            }
        """)
        self.centralwidget = QtWidgets.QWidget(TicTacToe)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 591, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ButtonsGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ButtonsGridLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonsGridLayout.setObjectName("ButtonsGridLayout")
        self.row1Col2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row1Col2.sizePolicy().hasHeightForWidth())
        self.row1Col2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.row1Col2.setFont(font)
        self.row1Col2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row1Col2.setAutoFillBackground(False)
        self.row1Col2.setObjectName("row1Col2")
        self.ButtonsGridLayout.addWidget(self.row1Col2, 0, 1, 1, 1)
        self.row3Col2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row3Col2.sizePolicy().hasHeightForWidth())
        self.row3Col2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.row3Col2.setFont(font)
        self.row3Col2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row3Col2.setAutoFillBackground(False)
        self.row3Col2.setObjectName("row3Col2")
        self.ButtonsGridLayout.addWidget(self.row3Col2, 2, 1, 1, 1)
        self.row2Col2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row2Col2.sizePolicy().hasHeightForWidth())
        self.row2Col2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.row2Col2.setFont(font)
        self.row2Col2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row2Col2.setAutoFillBackground(False)
        self.row2Col2.setObjectName("row2Col2")
        self.ButtonsGridLayout.addWidget(self.row2Col2, 1, 1, 1, 1)
        self.row1Col1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row1Col1.sizePolicy().hasHeightForWidth())
        self.row1Col1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.row1Col1.setFont(font)
        self.row1Col1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row1Col1.setAutoFillBackground(False)
        self.row1Col1.setObjectName("row1Col1")
        self.ButtonsGridLayout.addWidget(self.row1Col1, 0, 0, 1, 1)
        self.row3Col1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row3Col1.sizePolicy().hasHeightForWidth())
        self.row3Col1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.row3Col1.setFont(font)
        self.row3Col1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row3Col1.setAutoFillBackground(False)
        self.row3Col1.setObjectName("row3Col1")
        self.ButtonsGridLayout.addWidget(self.row3Col1, 2, 0, 1, 1)
        self.row2Col1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row2Col1.sizePolicy().hasHeightForWidth())
        self.row2Col1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.row2Col1.setFont(font)
        self.row2Col1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row2Col1.setAutoFillBackground(False)
        self.row2Col1.setObjectName("row2Col1")
        self.ButtonsGridLayout.addWidget(self.row2Col1, 1, 0, 1, 1)
        self.row1Col3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row1Col3.sizePolicy().hasHeightForWidth())
        self.row1Col3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.row1Col3.setFont(font)
        self.row1Col3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row1Col3.setAutoFillBackground(False)
        self.row1Col3.setObjectName("row1Col3")
        self.ButtonsGridLayout.addWidget(self.row1Col3, 0, 2, 1, 1)
        self.row2Col3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row2Col3.sizePolicy().hasHeightForWidth())
        self.row2Col3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.row2Col3.setFont(font)
        self.row2Col3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row2Col3.setAutoFillBackground(False)
        self.row2Col3.setObjectName("row2Col3")
        self.ButtonsGridLayout.addWidget(self.row2Col3, 1, 2, 1, 1)
        self.row3Col3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row3Col3.sizePolicy().hasHeightForWidth())
        self.row3Col3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.row3Col3.setFont(font)
        self.row3Col3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.row3Col3.setAutoFillBackground(False)
        self.row3Col3.setObjectName("row3Col3")
        self.ButtonsGridLayout.addWidget(self.row3Col3, 2, 2, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LabelLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.LabelLayout.setContentsMargins(0, 0, 0, 0)
        self.LabelLayout.setObjectName("LabelLayout")
        self.TextLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TextLabel.setFont(font)
        self.TextLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.TextLabel.setObjectName("TextLabel")
        self.LabelLayout.addWidget(self.TextLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.resetLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.resetLayoutWidget.setGeometry(QtCore.QRect(10, 370, 591, 50))
        self.resetLayoutWidget.setObjectName("resetLayoutWidget")
        
        self.ResetLayout = QtWidgets.QGridLayout(self.resetLayoutWidget)
        self.ResetLayout.setContentsMargins(0, 0, 0, 0)
        self.ResetLayout.setObjectName("ResetLayout")
        
        self.ResetButton = QtWidgets.QPushButton(self.resetLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.ResetButton.setFont(font)
        self.ResetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetButton.setAutoFillBackground(False)
        self.ResetButton.setObjectName("ResetButton")
        self.ResetLayout.addWidget(self.ResetButton, 0, 0, 1, 1)
        
        TicTacToe.resize(609, 430)
        TicTacToe.setMinimumSize(QtCore.QSize(609, 430))
        TicTacToe.setMaximumSize(QtCore.QSize(609, 430))
        
        TicTacToe.setCentralWidget(self.centralwidget)

        self.retranslateUi(TicTacToe)
        QtCore.QMetaObject.connectSlotsByName(TicTacToe)

        self.counter = 0
        self.row1Col2.clicked.connect(lambda: self.click_button(self.row1Col2))
        self.row3Col2.clicked.connect(lambda: self.click_button(self.row3Col2))
        self.row2Col2.clicked.connect(lambda: self.click_button(self.row2Col2))
        self.row1Col1.clicked.connect(lambda: self.click_button(self.row1Col1))
        self.row3Col1.clicked.connect(lambda: self.click_button(self.row3Col1))
        self.row2Col1.clicked.connect(lambda: self.click_button(self.row2Col1))
        self.row1Col3.clicked.connect(lambda: self.click_button(self.row1Col3))
        self.row2Col3.clicked.connect(lambda: self.click_button(self.row2Col3))
        self.row3Col3.clicked.connect(lambda: self.click_button(self.row3Col3))
        self.ResetButton.clicked.connect(self.reset_game)


    def retranslateUi(self, TicTacToe):
        _translate = QtCore.QCoreApplication.translate
        TicTacToe.setWindowTitle(_translate("TicTacToe", "TicTacToe"))
        self.row1Col2.setText(_translate("TicTacToe", ""))
        self.row3Col2.setText(_translate("TicTacToe", ""))
        self.row2Col2.setText(_translate("TicTacToe", ""))
        self.row1Col1.setText(_translate("TicTacToe", ""))
        self.row3Col1.setText(_translate("TicTacToe", ""))
        self.row2Col1.setText(_translate("TicTacToe", ""))
        self.row1Col3.setText(_translate("TicTacToe", ""))
        self.row2Col3.setText(_translate("TicTacToe", ""))
        self.row3Col3.setText(_translate("TicTacToe", ""))
        self.TextLabel.setText(_translate("TicTacToe", "Welcome to TicTacToe Owner: Muhammad Zaid"))
        self.ResetButton.setText(_translate("TicTacToe", "⟲"))

    def check_winner(self):
        #Check row 1
        if self.row1Col1.text() != '' and self.row1Col1.text() == self.row1Col2.text() and self.row1Col1.text() == self.row1Col3.text():
            self.win(self.row1Col1, self.row1Col2, self.row1Col3)
        #Check row 2
        elif self.row2Col1.text() != '' and self.row2Col1.text() == self.row2Col2.text() and self.row2Col1.text() == self.row2Col3.text():
            self.win(self.row2Col1, self.row2Col2, self.row2Col3)
        #Check row 3
        elif self.row3Col1.text() != '' and self.row3Col1.text() == self.row3Col2.text() and self.row3Col1.text() == self.row3Col3.text():
            self.win(self.row3Col1, self.row3Col2, self.row3Col3)
        #Check column 1
        elif self.row1Col1.text() != '' and self.row1Col1.text() == self.row2Col1.text() and self.row1Col1.text() == self.row3Col1.text():
            self.win(self.row1Col1, self.row2Col1, self.row3Col1)
        #Check column 2
        elif self.row1Col2.text() != '' and self.row1Col2.text() == self.row2Col2.text() and self.row1Col2.text() == self.row3Col2.text():
            self.win(self.row1Col2, self.row2Col2, self.row3Col2)
        #Check column 3
        elif self.row1Col3.text() != '' and self.row1Col3.text() == self.row2Col3.text() and self.row1Col3.text() == self.row3Col3.text():
            self.win(self.row1Col3, self.row2Col3, self.row3Col3)
        #Check diagonal 1
        elif self.row1Col1.text() != '' and self.row1Col1.text() == self.row2Col2.text() and self.row1Col1.text() == self.row3Col3.text():
            self.win(self.row1Col1, self.row2Col2, self.row3Col3)
        #Check diagonal 2
        elif self.row1Col3.text() != '' and self.row1Col3.text() == self.row2Col2.text() and self.row1Col3.text() == self.row3Col1.text():
            self.win(self.row1Col3, self.row2Col2, self.row3Col1)
        elif self.counter >= 9:
            self.TextLabel.setText("Game Over! No Winner")
            self.disable_buttons()

    def win(self, row1, row2, row3):
        win_style = """
            background-color: #4CAF50;
            color: white;
            border: 2px solid #45a049;
        """
        row1.setStyleSheet(win_style)
        row2.setStyleSheet(win_style)
        row3.setStyleSheet(win_style)
        self.TextLabel.setText(f"Congratulations! The Winner is {row1.text()}")
        self.disable_buttons()

    def disable_buttons(self):
        buttons = [self.row1Col1, self.row1Col2, self.row1Col3, self.row2Col1, self.row2Col2, self.row2Col3, self.row3Col1, self.row3Col2, self.row3Col3]
        for button in buttons:
            button.setEnabled(False)

    def click_button(self, button):
        if self.counter % 2 == 0:
            turn = 'X'
            self.TextLabel.setText(f"O's Turn")
        else:
            turn = 'O'
            self.TextLabel.setText(f"X's Turn")
        button.setText(turn)
        self.counter += 1
        self.check_winner()

    def reset_game(self):
        buttons = [self.row1Col1, self.row1Col2, self.row1Col3, self.row2Col1, self.row2Col2, self.row2Col3, self.row3Col1, self.row3Col2, self.row3Col3]
        for button in buttons:
            button.setText('')
            button.setStyleSheet('')
            button.setEnabled(True)
        self.TextLabel.setText("Welcome to TicTacToe Owner: Muhammad Zaid")
        self.counter = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TicTacToe = QtWidgets.QMainWindow()
    ui = Ui_TicTacToe()
    ui.setupUi(TicTacToe)
    TicTacToe.show()
    sys.exit(app.exec_())
