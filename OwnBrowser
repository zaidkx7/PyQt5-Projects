import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com/'))
        self.setCentralWidget(self.browser)

        #Nav Bar
        NavBar = QToolBar()
        self.addToolBar(NavBar)

        #add actions
        back_btn = QAction('←', self)
        back_btn.triggered.connect(self.browser.back)
        NavBar.addAction(back_btn)

        forward_btn = QAction('→', self)
        forward_btn.triggered.connect(self.browser.forward)
        NavBar.addAction(forward_btn)

        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        NavBar.addAction(reload_btn)

        navigateH = QAction('⌂', self)
        navigateH.triggered.connect(self.navigate_home)
        NavBar.addAction(navigateH)

        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.GotoUrl)
        NavBar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.urlchanged)

        youtubebtn = QAction('▶', self)
        youtubebtn.triggered.connect(self.Youtube_btn)
        NavBar.addAction(youtubebtn)






        self.showMaximized()

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com/'))

    def Youtube_btn(self):
        self.browser.setUrl(QUrl('http://Youtube.com/'))

    def GotoUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))

    def urlchanged(self, q):
        self.searchBar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("My Browser")
MW = MainWindow()
app.exec_()
