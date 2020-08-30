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

# categories and subcategories for api and ui
categories = ["Current Events", "Fine Arts", "Geography", "History", "Literature", "Mythology", "Philosophy", "Religion"
              , "Science", "Social Science", "Trash"]
categoriesID = [26, 21, 20, 18, 15, 14, 25, 19, 17, 22, 16]
subcategories = ["Current Events American", "Current Events Other", "Fine Arts American", "Fine Arts Audiovisual"
                 , "Fine Arts Auditory", "Fine Arts British", "Fine Arts European", "Fine Arts Opera", "Fine Arts Other"
                 , "Fine Arts Visual", "Fine Arts World", "Geography American", "Geography World", "History American"
                 , "History British", "History Classical", "History European", "History Other", "History World"
                 , "Literature American", "Literature British", "Literature Classical", "Literature European"
                 , "Literature Other", "Literature World", "Mythology American", "Mythology Chinese"
                 , "Mythology Egyptian", "Mythology Greco-Roman", "Mythology Indian", "Mythology Japanese"
                 , "Mythology Norse", "Mythology Other", "Mythology Other East Asian", "Philosophy American"
                 , "Philosophy Classical", "Philosophy East Asian", "Philosophy European", "Philosophy Other"
                 , "Religion American", "Religion Christianity", "Religion East Asian", "Religion Islam"
                 , "Religion Judaism", "Religion Other", "Science American", "Science Biology", "Science Chemistry"
                 , "Science Computer Science", "Science Math", "Science Other", "Science Physics", "Science World"
                 , "Social Science American", "Social Science Anthropology", "Social Science Economics"
                 , "Social Science Linguistics", "Social Science Other", "Social Science Political Science"
                 , "Social Science Psychology", "Social Science Sociology", "Trash American", "Trash Movies"
                 , "Trash Music", "Trash Other", "Trash Sports", "Trash Television", "Trash Video Games"]
subcategoriesID = [40, 42, 35, 27, 8, 45, 50, 77, 25, 2, 43, 38, 44, 13, 6, 16, 24, 28, 20, 4, 22, 30, 1, 29, 12, 33
                   , 47, 65, 58, 46, 48, 63, 54, 49, 39, 61, 52, 66, 74, 31, 57, 51, 68, 69, 62, 36, 14, 5, 23, 26, 10
                   , 18, 37, 34, 76, 56, 75, 60, 64, 71, 73, 32, 72, 67, 59, 55, 70, 53]


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
