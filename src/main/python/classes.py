from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class StartWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        # for centering window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # init window
        self.setWindowTitle("QuickBuzz")
        self.setGeometry(qtRectangle)
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        self.setStyleSheet("background-color: #FCF6BD;")
        self.setWindowIcon(QIcon("src/main/python/Icon.ico"))

        # title label
        self.titleLabel = QLabel(u"QuickBuzz\u2122", self)
        self.titleLabel.setFont(QFont('Helvetica Neue', 40))
        self.titleLabel.setStyleSheet("color: black; margin: 50px; font: bold")

        # buttons
        self.startButton = QPushButton()
        self.startButton.setText("Start Training")
        self.startButton.setFont(QFont('Helvetica Neue', 20))
        self.startButton.setFixedWidth(400)
        self.startButton.setStyleSheet("QPushButton {"
                                       "background-color: #D0F4DE;"
                                       "border-radius: 15px; "
                                       "padding: 15px; "
                                       "border-style: outset;"
                                       "margin: 25px"
                                       "}"
                                       "QPushButton:pressed {"
                                       "background-color: #A9DEF9;"
                                       "border-radius: 15px;"
                                       "padding:15px;"
                                       "border-style: inset;"
                                       "}")

        self.infoButton = QPushButton()
        self.infoButton.setText("Information")
        self.infoButton.setFont(QFont('Helvetica Neue', 20))
        self.infoButton.setFixedWidth(400)
        self.infoButton.setStyleSheet("QPushButton {"
                                       "background-color: #D0F4DE;"
                                       "border-radius: 15px; "
                                       "padding: 15px; "
                                       "border-style: outset;"
                                       "margin: 25px"
                                       "}"
                                       "QPushButton:pressed {"
                                       "background-color: #A9DEF9;"
                                       "border-radius: 15px;"
                                       "padding:15px;"
                                       "border-style: inset;"
                                       "}")
        self.infoButton.clicked.connect(self.infoNavigate)
        self.startButton.clicked.connect(self.gameNavigate)
        # putting it together
        self.widget = QWidget(self)
        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.titleLabel, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.startButton, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.infoButton, alignment=Qt.AlignCenter)
        self.layout.addStretch()
        self.setCentralWidget(self.widget)

        self.show()

    def infoNavigate(self):
        self.infowindow = InfoWindow()
        self.infowindow.show()
        self.close()

    def gameNavigate(self):
        self.gamewindow = GamePlay()
        self.gamewindow.show()
        self.close()



class InfoWindow(QMainWindow):

    def __init__(self):
        super().__init__()



        # for centering window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # init window
        self.setWindowTitle("QuickBuzz")
        self.setGeometry(qtRectangle)
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        self.setStyleSheet("background-color: #FCF6BD;")
        self.setWindowIcon(QIcon("src/main/python/Icon.ico"))

        # title label
        self.titleLabel = QLabel(u"QuickBuzz\u2122", self)
        self.titleLabel.setFont(QFont('Helvetica Neue', 40))
        self.titleLabel.setStyleSheet("color: black; margin: 50px; font: bold")

        # information label
        self.infoLabel = QLabel("QuickBuzz is a Quizbowl trainer application. "
                                "The application allows you to train against a bot. "
                                "Questions are drawn from the QuizDB database. "
                                "You can filter questions and also set the number of questions you would like to play. "
                                "This application was written in PyQt5 by Spandan Goel. "
                                "Happy Training!")
        self.infoLabel.setFont(QFont('Helvetica Neue', 12))
        self.infoLabel.setStyleSheet("color: black; margin: 20px; font: bold")
        self.infoLabel.setWordWrap(True)

        # buttons
        self.backButton = QPushButton()
        self.backButton.setText("Back")
        self.backButton.setFont(QFont('Helvetica Neue', 20))
        self.backButton.setFixedWidth(400)
        self.backButton.setStyleSheet("QPushButton {"
                                      "background-color: #D0F4DE;"
                                      "border-radius: 15px; "
                                      "padding: 15px; "
                                      "border-style: outset;"
                                      "margin: 25px"
                                      "}"
                                      "QPushButton:pressed {"
                                      "background-color: #A9DEF9;"
                                      "border-radius: 15px;"
                                      "padding:15px;"
                                      "border-style: inset;"
                                      "}")
        self.backButton.clicked.connect(self.back)

        # putting it together
        self.widget = QWidget(self)
        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.titleLabel, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.infoLabel, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.backButton, alignment=Qt.AlignCenter)
        self.layout.addStretch()
        self.setCentralWidget(self.widget)

    def back(self):
        self.hide()
        self.startwindow = StartWindow()
        self.startwindow.show()


categories = []
categoriesID = []
subcategories = []
subcategoriesID = []

class GamePlay(QMainWindow):
    def __init__(self):
        super().__init__()

        # for centering window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # init window
        self.setWindowTitle("QuickBuzz")
        self.setGeometry(qtRectangle)
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        self.setStyleSheet("background-color: #F9ADA0;")
        self.setWindowIcon(QIcon("src/main/python/Icon.ico"))

        # dropdowns for category and subcategory


        # putting it together
        self.widget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.widget)
        self.firstHor = QHBoxLayout()

        self.firstHor.addWidget()


        self.mainLayout.addLayout(self.firstHor)

        self.setCentralWidget(self.widget)

    def back(self):
        self.hide()
        self.startwindow = StartWindow()
        self.startwindow.show()