import random
import threading
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

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
        self.gamewindow = CategorySelection()
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
              , "Science", "Social Studies", "Trash", "Everything"]
categoriesID = [26, 21, 20, 18, 15, 14, 25, 19, 17, 22, 16, -1]
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
                 , "Social Studies American", "Social Studies Anthropology", "Social Studies Economics"
                 , "Social Studies Linguistics", "Social Studies Other", "Social Studies Political Studies"
                 , "Social Studies Psychology", "Social Studies Sociology", "Trash American", "Trash Movies"
                 , "Trash Music", "Trash Other", "Trash Sports", "Trash Television", "Trash Video Games"
                 , "Everything"]
subcategoriesID = [40, 42, 35, 27, 8, 45, 50, 77, 25, 2, 43, 38, 44, 13, 6, 16, 24, 28, 20, 4, 22, 30, 1, 29, 12, 33
                   , 47, 65, 58, 46, 48, 63, 54, 49, 39, 61, 52, 66, 74, 31, 57, 51, 68, 69, 62, 36, 14, 5, 23, 26, 10
                   , 18, 37, 34, 76, 56, 75, 60, 64, 71, 73, 32, 72, 67, 59, 55, 70, 53, -1]
difficulties = ["1) Middle School", "2) Easy High School", "3) Regular High School", "4) Hard High School"
                , "5) National High School", "6) Easy College", "7) Regular College", "8) Hard College", "9) Open"
                , "10) Everything"]
difficultiesID = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
selectedCategories = []
selectedCategoryButtons = []
selectedSubCategories = []
selectedSubCategoryButtons = []
selectedDifficulties = []
selectedDifficultiesButtons = []


class CategorySelection(QMainWindow):
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
        self.categoryDrop = QComboBox(self)
        for i in categories:
            if i not in selectedCategories:
                self.categoryDrop.addItem(i)
        self.categoryDropLabel = QLabel("Category")
        self.categoryDrop.activated[str].connect(self.dropDownChangedCategory)
        self.categoryDrop.setFont(QFont("Helvetica Neue", 14))
        self.categoryDrop.setFixedWidth(200)
        self.categoryDrop.setStyleSheet("border: 5px black; background: #E4C1F9; height: 50px;")


        # buttons for removing category/subcategory
        self.rmCat = QPushButton()
        self.rmCat.setText("Remove Category")
        self.rmCat.setFont(QFont('Helvetica Neue', 12))
        self.rmCat.setFixedWidth(200)
        self.rmCat.setStyleSheet("QPushButton {"
                                 "background-color: #FCF6BD;"
                                 "border-radius: 15px; "
                                 "padding: 5px; "
                                 "border-style: outset;"
                                 "margin: 5px"
                                 "}"
                                 "QPushButton:pressed {"
                                 "background-color: #E4C1F9;"
                                 "border-radius: 15px;"
                                 "padding:5px;"
                                 "border-style: inset;"
                                 "}")
        self.rmCat.clicked.connect(self.removeCat)

        # navigation buttons
        self.backButton = QPushButton()
        self.backButton.setText("Back")
        self.backButton.setFont(QFont('Helvetica Neue', 20))
        self.backButton.setFixedWidth(200)
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

        self.nextButton = QPushButton()
        self.nextButton.setText("Next")
        self.nextButton.setFont(QFont('Helvetica Neue', 20))
        self.nextButton.setFixedWidth(200)
        self.nextButton.setStyleSheet("QPushButton {"
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
        self.nextButton.clicked.connect(self.next)

        # putting it together
        self.widget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.widget)

        self.zeroHor = QHBoxLayout()
        self.zeroHor.addWidget(self.rmCat)

        self.firstHor = QHBoxLayout()
        self.firstHor.addWidget(self.categoryDrop)

        self.secondHor = QGridLayout()
        self.gridx = 0
        self.gridy = 0

        for i in selectedCategoryButtons:
            if "Everything" in selectedCategories:
                self.categoryDrop.clear()
            self.secondHor.addWidget(i, self.gridx, self.gridy)
            self.gridy += 1
            if self.gridy % 5 == 0 and self.gridy > 0:
                self.gridx += 1
                self.gridy = self.gridy % 5

        self.thirdHor = QHBoxLayout()
        self.thirdHor.addWidget(self.backButton)
        self.thirdHor.addWidget(self.nextButton)

        self.mainLayout.addLayout(self.zeroHor)
        self.mainLayout.addLayout(self.firstHor)
        self.mainLayout.addLayout(self.secondHor)
        self.mainLayout.addLayout(self.thirdHor)
        self.setCentralWidget(self.widget)

    def dropDownChangedCategory(self, text):
        self.categoryDrop.adjustSize()
        self.categoryDrop.clear()
        global selectedCategories, selectedCategoryButtons
        selectedCategories.append(text)
        for i in categories:
            if "Everything" in selectedCategories:
                selectedCategories = ["Everything"]
                selectedCategoryButtons = []
                break
            if i not in selectedCategories:
                if i != "Everything":
                    self.categoryDrop.addItem(i)

        self.tempButton = QPushButton()
        self.tempButton.setText(text)
        self.tempButton.setFont(QFont('Helvetica Neue', 8))
        self.tempButton.setFixedWidth(100)
        self.tempButton.setStyleSheet("QPushButton {"
                                      "background-color: #D0F4DE;"
                                      "border-radius: 15px; "
                                      "padding: 5px; "
                                      "border-style: outset;"
                                      "margin: 5px"
                                      "}"
                                      "QPushButton:pressed {"
                                      "background-color: #A9DEF9;"
                                      "border-radius: 15px;"
                                      "padding:5px;"
                                      "border-style: inset;"
                                      "}")
        self.secondHor.addWidget(self.tempButton, self.gridx, self.gridy)
        self.gridy += 1
        if self.gridy % 5 == 0 and self.gridy > 0:
            self.gridx += 1
            self.gridy = self.gridy % 5
        selectedCategoryButtons.append(self.tempButton)

    def removeCat(self):
        try:
            selectedCategoryButtons[len(selectedCategoryButtons)-1].hide()
            selectedCategoryButtons.pop()
            selectedCategories.pop()
            if self.gridy != 0:
                self.gridy -= 1
            elif self.gridy == 0 and self.gridx != 0:
                self.gridx -= 1
                self.gridy = 4
        except:
            catReply = QMessageBox()
            catReply.setIcon(QMessageBox.Warning)
            catReply.setWindowTitle("QuickBuzz")
            catReply.setText("There are no categories to remove")
            catReply.setStandardButtons(QMessageBox.Ok)

            returnValue = catReply.exec()


        self.categoryDrop.clear()
        for i in categories:
            if "Everything" in selectedCategories:
                break
            if i not in selectedCategories:
                if i != "Everything":
                    self.categoryDrop.addItem(i)

        if selectedCategories == []:
            self.categoryDrop.addItem("Everything")


    def back(self):
        self.hide()
        self.startwindow = StartWindow()
        self.startwindow.show()
        self.gridx = 0
        self.gridy = 0
    def next(self):
        self.hide()
        self.nextwindow = SubCategorySelection()
        self.nextwindow.show()
        self.gridx = 0
        self.gridy = 0

class SubCategorySelection(QMainWindow):
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

        self.subCategoryDrop = QComboBox(self)
        if "Everything" not in selectedCategories:
            for i in selectedCategories:
                for j in subcategories:
                    if i in j:
                        self.subCategoryDrop.addItem(j)
                self.subCategoryDrop.addItem("Everything " + i)

        self.subCategoryDrop.activated[str].connect(self.dropDownChangedSubCategory)
        self.subCategoryDrop.setFont(QFont("Helvetica Neue", 14))
        self.subCategoryDrop.setFixedWidth(370)
        self.subCategoryDrop.setStyleSheet("border: 5px black; background: #E4C1F9; height: 50px;")

        self.rmSubCat = QPushButton()
        self.rmSubCat.setText("Remove Subcategory")
        self.rmSubCat.setFont(QFont('Helvetica Neue', 12))
        self.rmSubCat.setFixedWidth(250)
        self.rmSubCat.setStyleSheet("QPushButton {"
                                 "background-color: #FCF6BD;"
                                 "border-radius: 15px; "
                                 "padding: 5px; "
                                 "border-style: outset;"
                                 "margin: 5px"
                                 "}"
                                 "QPushButton:pressed {"
                                 "background-color: #E4C1F9;"
                                 "border-radius: 15px;"
                                 "padding:5px;"
                                 "border-style: inset;"
                                 "}")
        self.rmSubCat.clicked.connect(self.removeSubCat)
        # navigation buttons
        self.backButton = QPushButton()
        self.backButton.setText("Back")
        self.backButton.setFont(QFont('Helvetica Neue', 20))
        self.backButton.setFixedWidth(200)
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

        self.nextButton = QPushButton()
        self.nextButton.setText("Next")
        self.nextButton.setFont(QFont('Helvetica Neue', 20))
        self.nextButton.setFixedWidth(200)
        self.nextButton.setStyleSheet("QPushButton {"
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
        self.nextButton.clicked.connect(self.next)

        # putting it together
        self.widget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.widget)

        self.zeroHor = QHBoxLayout()
        self.zeroHor.addWidget(self.rmSubCat)

        self.firstHor = QHBoxLayout()
        self.firstHor.addWidget(self.subCategoryDrop)

        self.secondHor = QGridLayout()
        self.gridx = 0
        self.gridy = 0

        self.thirdHor = QHBoxLayout()
        self.thirdHor.addWidget(self.backButton)
        self.thirdHor.addWidget(self.nextButton)

        self.mainLayout.addLayout(self.zeroHor)
        self.mainLayout.addLayout(self.firstHor)
        self.mainLayout.addLayout(self.secondHor)
        self.mainLayout.addLayout(self.thirdHor)
        self.setCentralWidget(self.widget)

    def dropDownChangedSubCategory(self, text):
        if "Everything" not in text:
            temp = text.split(" ")
            for i in range(self.subCategoryDrop.count()):
                if "Everything" in self.subCategoryDrop.itemText(i) and temp[0] in self.subCategoryDrop.itemText(i):
                    self.subCategoryDrop.removeItem(i)
        if "Everything" in text:
            temp = text.split(" ")
            i = self.subCategoryDrop.count()
            while i >= 0:
                if temp[1] in self.subCategoryDrop.itemText(i):
                    self.subCategoryDrop.removeItem(i)
                    i+=1
                i-=1

        for i in range(self.subCategoryDrop.count()):
            if self.subCategoryDrop.itemText(i) == text:
                self.subCategoryDrop.removeItem(i)

        selectedSubCategories.append(text)


        self.tempButton = QPushButton()
        self.tempButton.setText(text)
        self.tempButton.setFont(QFont('Helvetica Neue', 4))
        self.tempButton.setFixedWidth(100)
        self.tempButton.setStyleSheet("QPushButton {"
                                      "background-color: #D0F4DE;"
                                      "border-radius: 15px; "
                                      "padding: 5px; "
                                      "border-style: outset;"
                                      "margin: 5px"
                                      "}"
                                      "QPushButton:pressed {"
                                      "background-color: #A9DEF9;"
                                      "border-radius: 15px;"
                                      "padding:5px;"
                                      "border-style: inset;"
                                      "}")
        self.secondHor.addWidget(self.tempButton, self.gridx, self.gridy)
        self.gridy += 1
        if self.gridy % 5 == 0 and self.gridy > 0:
            self.gridx += 1
            self.gridy = self.gridy % 5
        selectedSubCategoryButtons.append(self.tempButton)

    def removeSubCat(self):
        try:

            removedEv = False
            whatremoved = ""
            if "Everything" in selectedSubCategories[len(selectedSubCategories)-1]:
                removedEv = True
                whatremoved = selectedSubCategories[len(selectedSubCategories)-1].split(" ")[1]

            selectedSubCategoryButtons[len(selectedSubCategoryButtons)-1].hide()
            selectedSubCategoryButtons.pop()
            if not removedEv:
                self.subCategoryDrop.addItem(selectedSubCategories[len(selectedSubCategories)-1])
            selectedSubCategories.pop()
            if self.gridy != 0:
                self.gridy -= 1
            elif self.gridy == 0 and self.gridx != 0:
                self.gridx -= 1
                self.gridy = 4
            if selectedSubCategories == [] and removedEv:
                if "Everything" in selectedCategories:
                    self.subCategoryDrop.addItem("Everything")
                else:
                    for i in selectedCategories:
                        for j in subcategories:
                            if i in j and whatremoved in j:
                                self.subCategoryDrop.addItem(j)
                        self.subCategoryDrop.addItem("Everything " + i)
            else:
                availableSubcats = []
                for j in range(self.subCategoryDrop.count()):
                    availableSubcats.append(self.subCategoryDrop.itemText(j))
                for i in selectedCategories:
                    addevery = True
                    everytemp = "Everything " + i
                    if everytemp not in availableSubcats:
                        for j in selectedSubCategories:
                            if i in j:
                                addevery = False
                        if addevery:
                            self.subCategoryDrop.addItem(everytemp)
        except:

            catReply = QMessageBox()
            catReply.setIcon(QMessageBox.Warning)
            catReply.setWindowTitle("QuickBuzz")
            catReply.setText("There are no subcategories to remove")
            catReply.setStandardButtons(QMessageBox.Ok)

            returnValue = catReply.exec()



    def back(self):
        self.hide()
        self.startwindow = CategorySelection()
        self.startwindow.show()

    def next(self):
        self.hide()
        self.diffwindow = DifficultySelection()
        self.diffwindow.show()


class DifficultySelection(QMainWindow):
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

        self.diffDrop = QComboBox(self)
        for i in difficulties:
            self.diffDrop.addItem(i)

        self.diffDrop.activated[str].connect(self.dropDownChangedDifficulty)
        self.diffDrop.setFont(QFont("Helvetica Neue", 14))
        self.diffDrop.setFixedWidth(370)
        self.diffDrop.setStyleSheet("border: 5px black; background: #E4C1F9; height: 50px;")

        self.rmDiff = QPushButton()
        self.rmDiff.setText("Remove Difficulty")
        self.rmDiff.setFont(QFont('Helvetica Neue', 12))
        self.rmDiff.setFixedWidth(250)
        self.rmDiff.setStyleSheet("QPushButton {"
                                 "background-color: #FCF6BD;"
                                 "border-radius: 15px; "
                                 "padding: 5px; "
                                 "border-style: outset;"
                                 "margin: 5px"
                                 "}"
                                 "QPushButton:pressed {"
                                 "background-color: #E4C1F9;"
                                 "border-radius: 15px;"
                                 "padding:5px;"
                                 "border-style: inset;"
                                 "}")
        self.rmDiff.clicked.connect(self.removeDiff)
        # navigation buttons
        self.backButton = QPushButton()
        self.backButton.setText("Back")
        self.backButton.setFont(QFont('Helvetica Neue', 20))
        self.backButton.setFixedWidth(200)
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

        self.nextButton = QPushButton()
        self.nextButton.setText("Confirm")
        self.nextButton.setFont(QFont('Helvetica Neue', 20))
        self.nextButton.setFixedWidth(300)
        self.nextButton.setStyleSheet("QPushButton {"
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
        self.nextButton.clicked.connect(self.next)

        # putting it together
        self.widget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.widget)

        self.zeroHor = QHBoxLayout()
        self.zeroHor.addWidget(self.rmDiff)

        self.firstHor = QHBoxLayout()
        self.firstHor.addWidget(self.diffDrop)

        self.secondHor = QGridLayout()
        self.gridx = 0
        self.gridy = 0

        self.thirdHor = QHBoxLayout()
        self.thirdHor.addWidget(self.backButton)
        self.thirdHor.addWidget(self.nextButton)

        self.mainLayout.addLayout(self.zeroHor)
        self.mainLayout.addLayout(self.firstHor)
        self.mainLayout.addLayout(self.secondHor)
        self.mainLayout.addLayout(self.thirdHor)
        self.setCentralWidget(self.widget)

    def dropDownChangedDifficulty(self, text):
        if "Everything" not in text:
            for i in range(self.diffDrop.count()):
                if "Everything" in self.diffDrop.itemText(i) or text == self.diffDrop.itemText(i):
                    self.diffDrop.removeItem(i)
        else:
            self.diffDrop.clear()



        selectedDifficulties.append(text)

        self.tempButton = QPushButton()
        self.tempButton.setText(text)
        self.tempButton.setFont(QFont('Helvetica Neue', 4))
        self.tempButton.setFixedWidth(100)
        self.tempButton.setStyleSheet("QPushButton {"
                                      "background-color: #D0F4DE;"
                                      "border-radius: 15px; "
                                      "padding: 5px; "
                                      "border-style: outset;"
                                      "margin: 5px"
                                      "}"
                                      "QPushButton:pressed {"
                                      "background-color: #A9DEF9;"
                                      "border-radius: 15px;"
                                      "padding:5px;"
                                      "border-style: inset;"
                                      "}")
        self.secondHor.addWidget(self.tempButton, self.gridx, self.gridy)
        self.gridy += 1
        if self.gridy % 5 == 0 and self.gridy > 0:
            self.gridx += 1
            self.gridy = self.gridy % 5
        selectedDifficultiesButtons.append(self.tempButton)

    def removeDiff(self):
        try:

            if "Everything" in selectedDifficulties[len(selectedDifficulties)-1]:
                self.diffDrop.clear()
                for i in difficulties:
                    self.diffDrop.addItem(i)
            else:
                self.diffDrop.addItem(selectedDifficulties[len(selectedDifficulties)-1])

            selectedDifficultiesButtons[len(selectedDifficultiesButtons)-1].hide()
            selectedDifficultiesButtons.pop()
            selectedDifficulties.pop()
            if self.gridy != 0:
                self.gridy -= 1
            elif self.gridy == 0 and self.gridx != 0:
                self.gridx -= 1
                self.gridy = 4


            if selectedDifficulties == []:
                self.diffDrop.addItem("Everything")
        except:

            catReply = QMessageBox()
            catReply.setIcon(QMessageBox.Warning)
            catReply.setWindowTitle("QuickBuzz")
            catReply.setText("There are no difficulties to remove")
            catReply.setStandardButtons(QMessageBox.Ok)

            returnValue = catReply.exec()




    def back(self):
        self.hide()
        self.startwindow = SubCategorySelection()
        self.startwindow.show()

    def next(self):
        self.hide()
        self.tuwindow = FindTossup()
        self.tuwindow.show()

availableTossupIDS = []
availableTossups = []
availableAnswers = []
availableTossupCategories = []

class FindTossup(QMainWindow):
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

        self.titleLabel = QLabel(u"Tossups", self)
        self.titleLabel.setFont(QFont('Helvetica Neue', 24))
        self.titleLabel.setStyleSheet("color: black; margin: 50px;")

        self.ftu = QPushButton()
        self.ftu.setText("Find Tossups")
        self.ftu.setFont(QFont('Helvetica Neue', 12))
        self.ftu.setFixedWidth(250)
        self.ftu.setStyleSheet("QPushButton {"
                                  "background-color: #FCF6BD;"
                                  "border-radius: 15px; "
                                  "padding: 5px; "
                                  "border-style: outset;"
                                  "margin: 5px"
                                  "}"
                                  "QPushButton:pressed {"
                                  "background-color: #E4C1F9;"
                                  "border-radius: 15px;"
                                  "padding:5px;"
                                  "border-style: inset;"
                                  "}")
        self.ftu.clicked.connect(self.getTUS)

        # putting it together
        self.widget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.widget)
        self.mainLayout.addWidget(self.titleLabel, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.ftu, alignment=Qt.AlignCenter)
        self.setCentralWidget(self.widget)

    def getTUS(self):
        strippedDiffs = []
        for i in selectedDifficulties:
            if i[0:2] == "10":
                strippedDiffs.append(10)
                break
            else:
                strippedDiffs.append(int(i[0:1]))
        if "Everything" in selectedCategories:
            for file in os.listdir("quizdb"):
                filename = os.fsdecode(file)
                with open(f"quizdb/{filename}", mode="r") as f:
                    data = f.readlines()
                    for j in range(0, len(data)):
                        if "-)" in data[j]:
                            id = data[j]
                            try:
                                dif = int(data[j + 3])
                                tu = data[j+1]
                                an = data[j+2]
                                ca = filename.partition(".")[0]
                            except ValueError:
                                continue
                            if dif in strippedDiffs or strippedDiffs == [10]:
                                availableTossupIDS.append(id)
                                availableTossups.append(tu)
                                availableAnswers.append(an)
                                availableTossupCategories.append(ca)
        else:
            for i in selectedSubCategories:
                if "Everything" in i:
                    temp = i.split(" ")
                    for file in os.listdir("quizdb"):
                        filename = os.fsdecode(file)
                        if temp[1] in filename:
                            with open(f"quizdb/{filename}", mode="r") as f:
                                data = f.readlines()
                                for j in range(0, len(data)):
                                    if "-)" in data[j]:
                                        id = data[j]
                                        try:
                                            dif = int(data[j + 3])
                                            tu = data[j+1]
                                            an = data[j+2]
                                            ca = filename.partition(".")[0]
                                        except ValueError:
                                            continue
                                        if dif in strippedDiffs or strippedDiffs == [10]:
                                            availableTossupIDS.append(id)
                                            availableTossups.append(tu)
                                            availableAnswers.append(an)
                                            availableTossupCategories.append(ca)
                else:
                    for file in os.listdir("quizdb"):
                        filename = os.fsdecode(file)
                        if i in filename:
                            with open(f"quizdb/{filename}", mode="r") as f:
                                data = f.readlines()
                                for j in range(0, len(data)):
                                    if "-)" in data[j]:
                                        id = data[j]
                                        try:
                                            dif = int(data[j + 3])
                                            tu = data[j+1]
                                            an = data[j+2]
                                            ca = filename.partition(".")[0]
                                        except ValueError:
                                            continue
                                        if dif in strippedDiffs or strippedDiffs == [10]:
                                            availableTossupIDS.append(id)
                                            availableTossups.append(tu)
                                            availableAnswers.append(an)
                                            availableTossupCategories.append(ca)

        self.doneLabel = QLabel(f"{len(availableTossupIDS)} Tossups Found", self)
        self.doneLabel.setFont(QFont('Helvetica Neue', 24))
        self.doneLabel.setStyleSheet("color: black; margin: 50px;")
        self.mainLayout.addWidget(self.doneLabel, alignment=Qt.AlignCenter)

        self.nextButton = QPushButton()
        self.nextButton.setText("Next")
        self.nextButton.setFont(QFont('Helvetica Neue', 20))
        self.nextButton.setFixedWidth(300)
        self.nextButton.setStyleSheet("QPushButton {"
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
        self.nextButton.clicked.connect(self.next)
        self.mainLayout.addWidget(self.nextButton, alignment=Qt.AlignCenter)

    def next(self):
        self.gameWin = SetupGame()
        self.gameWin.show()
        self.hide()

numOfTu = 0
gameTossups = []
gameAnswers = []
gameTossupCategories = []
gameTossupIDs = []
botDiff = 1

class SetupGame(QMainWindow):
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

        self.titleLabel = QLabel(u"Bot Settings", self)
        self.titleLabel.setFont(QFont('Helvetica Neue', 24))
        self.titleLabel.setStyleSheet("color: black; margin: 50px;")

        self.numTossups, self.okPressed = QInputDialog.getInt(self, "Number of Tossups", "Tossups to play:", 20, 1,
                                                              len(availableTossups), 1)


        self.diffRadio1 = QRadioButton("I'm too immature to lose")
        self.diffRadio1.setChecked(True)
        self.diffRadio1.diff = 1
        self.diffRadio1.toggled.connect(self.diffClicked)
        self.diffRadio1.setStyleSheet("font: 18pt Helvetica Neue")

        self.diffRadio2 = QRadioButton("Noob")
        self.diffRadio2.setChecked(False)
        self.diffRadio2.diff = 2
        self.diffRadio2.toggled.connect(self.diffClicked)
        self.diffRadio2.setStyleSheet("font: 18pt Helvetica Neue")

        self.diffRadio3 = QRadioButton("Mediocre")
        self.diffRadio3.setChecked(False)
        self.diffRadio3.diff = 3
        self.diffRadio3.toggled.connect(self.diffClicked)
        self.diffRadio3.setStyleSheet("font: 18pt Helvetica Neue")

        self.diffRadio4 = QRadioButton("Captain")
        self.diffRadio4.setChecked(False)
        self.diffRadio4.diff = 4
        self.diffRadio4.toggled.connect(self.diffClicked)
        self.diffRadio4.setStyleSheet("font: 18pt Helvetica Neue")

        self.diffRadio5 = QRadioButton("Pro")
        self.diffRadio5.setChecked(False)
        self.diffRadio5.diff = 5
        self.diffRadio5.toggled.connect(self.diffClicked)
        self.diffRadio5.setStyleSheet("font: 18pt Helvetica Neue")

        self.nextButton = QPushButton()
        self.nextButton.setText("Start Training")
        self.nextButton.setFont(QFont('Helvetica Neue', 20))
        self.nextButton.setFixedWidth(400)
        self.nextButton.setStyleSheet("QPushButton {"
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
        self.nextButton.clicked.connect(self.next)

        # putting it together
        self.widget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.widget)
        self.mainLayout.addWidget(self.titleLabel, alignment=Qt.AlignCenter)

        self.radioLayout = QGridLayout()
        self.mainLayout.addLayout(self.radioLayout)

        self.radioLayout.addWidget(self.diffRadio1, 1, 0)
        self.radioLayout.addWidget(self.diffRadio2, 2, 0)
        self.radioLayout.addWidget(self.diffRadio3, 3, 0)
        self.radioLayout.addWidget(self.diffRadio4, 4, 0)
        self.radioLayout.addWidget(self.diffRadio5, 5, 0)

        self.mainLayout.addWidget(self.nextButton, alignment=Qt.AlignCenter)
        self.setCentralWidget(self.widget)
        self.facilitator()
    def facilitator(self):
        if self.okPressed and len(availableTossups) != 0:
            randomTossupIndexes = random.sample(range(0,len(availableTossups)), self.numTossups)
            for i in randomTossupIndexes:
                gameTossups.append(availableTossups[i])
                gameAnswers.append(availableAnswers[i])
                gameTossupIDs.append(availableTossupIDS[i])
                gameTossupCategories.append(availableTossupCategories[i])
        else:
            catReply = QMessageBox()
            catReply.setIcon(QMessageBox.Warning)
            catReply.setWindowTitle("QuickBuzz")
            catReply.setText("There are no tossups to play. Closing application")
            self.close()
            catReply.setStandardButtons(QMessageBox.Ok)
            returnValue = catReply.exec()
            if returnValue == QMessageBox.Ok:
                self.close()
                sys.exit()

    def diffClicked(self):
        self.diffRadio = self.sender()
        global botDiff
        botDiff = self.diffRadio.diff

    def next(self):
        self.hide()
        self.startTrainWindow = TrainWindow()
        self.startTrainWindow.show()


class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        self.label.setFont(QFont('Helvetica Neue', 8))
        # adding label to the layout
        lay.addWidget(self.label)

        # the setText method

    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

botScore = 0
meScore = 0
botScoreByTossup = []
meScoreByTossup = []
botQDepth = []
meQDepth = []

statusString = ""

class TrainWindow(QMainWindow):
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
        self.setFixedHeight(700)
        self.setStyleSheet("background-color: #D0F4DE;")
        self.setWindowIcon(QIcon("src/main/python/Icon.ico"))

        self.questionLabel = QLabel("", self)
        self.questionLabel.setFont(QFont('Helvetica Neue', 10))
        self.questionLabel.setStyleSheet("color: black; margin-right: 10px; margin-left: 10px; border: 1px solid black")
        self.questionLabel.setWordWrap(True)
        self.questionLabel.setFixedHeight(300)

        self.tossupLabel = QLabel("", self)
        self.tossupLabel.setFont(QFont('Helvetica Neue', 8))
        self.tossupLabel.setStyleSheet("color: black; margin-right: 10px; margin-left: 10px; border: 1px solid black")
        self.tossupLabel.setWordWrap(True)
        self.tossupLabel.setFixedHeight(25)

        self.answerLabel = QLabel("", self)
        self.answerLabel.setFont(QFont('Helvetica Neue', 8))
        self.answerLabel.setStyleSheet("color: black; margin-right: 10px; margin-left: 10px; border: 1px solid black;"
                                       "font: bold")
        self.answerLabel.setWordWrap(True)
        self.answerLabel.setFixedHeight(25)

        self.humanTag = QLabel("You", self)
        self.humanTag.setFont(QFont('Helvetica Neue', 8))
        self.humanTag.setStyleSheet("color: black; margin-left: 10px; margin-top: 5px;"
                                    "border: solid black;"
                                    "border-width: 1px 0px 1px 1px;")
        self.humanTag.setFixedHeight(25)
        self.humanTag.setFixedWidth(120)
        self.humanTag.setAlignment(Qt.AlignLeft)

        self.scorehuman = QLabel(f"{meScore}", self)
        self.scorehuman.setFont(QFont('Helvetica Neue', 8))
        self.scorehuman.setStyleSheet("color: black; margin-top: 5px;"
                                      "border: solid black;"
                                      "border-width: 1px 1px 1px 0px;")
        self.scorehuman.setFixedHeight(25)
        self.scorehuman.setFixedWidth(120)
        self.scorehuman.setAlignment(Qt.AlignRight)

        self.tossupTimer = QLabel("Tossup")
        self.tossupTimer.setFont(QFont('Helvetica Neue', 8))
        self.tossupTimer.setStyleSheet("color: black; margin-top: 5px;"
                                       "border: solid black;"
                                       "border-width: 1px 0px 1px 1px")
        self.tossupTimer.setFixedHeight(25)
        self.tossupTimer.setFixedWidth(100)
        self.tossupTimer.setAlignment(Qt.AlignCenter)

        self.scorebot = QLabel(f"{botScore}", self)
        self.scorebot.setFont(QFont('Helvetica Neue', 8))
        self.scorebot.setStyleSheet("color: black; margin-top: 5px;"
                                    "border: solid black;"
                                    "border-width: 1px 0px 1px 1px;")
        self.scorebot.setFixedHeight(25)
        self.scorebot.setFixedWidth(120)
        self.scorebot.setAlignment(Qt.AlignLeft)

        self.botTag = QLabel(f"Bot {botDiff}", self)
        self.botTag.setFont(QFont('Helvetica Neue', 8))
        self.botTag.setStyleSheet("color: black; margin-right: 10px; margin-top: 5px;"
                                  "border: solid black;"
                                  "border-width: 1px 1px 1px 0px;")
        self.botTag.setFixedHeight(25)
        self.botTag.setFixedWidth(120)
        self.botTag.setAlignment(Qt.AlignRight)

        self.statusWindow = ScrollLabel()
        self.statusWindow.setText(f"{statusString}")
        self.statusWindow.setStyleSheet("color: black; margin-right: 10px; margin-left: 10px; margin-top:5px;")
        self.statusWindow.setFixedHeight(170)
        self.statusWindow.setFixedWidth(580)

        self.buzzButton = QPushButton()
        self.buzzButton.setText("Buzz")
        self.buzzButton.setFont(QFont('Helvetica Neue', 20))
        self.buzzButton.setFixedWidth(580)
        self.buzzButton.setStyleSheet("QPushButton {"
                                      "background-color: #E4C1F9;"
                                      "padding: 15px; "
                                      "border-style: outset;"
                                      "margin: 10px"
                                      "}"
                                      "QPushButton:pressed {"
                                      "background-color: #A9DEF9;"
                                      "padding:15px;"
                                      "border-style: inset;"
                                      "}")
        self.buzzButton.clicked.connect(self.meBuzz)

        self.answerBox = QLineEdit(self)
        self.answerBox.setFont(QFont('Helvetica Neue', 20))
        self.answerBox.setFixedWidth(410)
        self.answerBox.setDisabled(True)
        self.answerBox.setStyleSheet("margin: 10px; padding: 5px;")
        self.answerBox.setPlaceholderText("Answer")
        self.answerBox.setFixedHeight(75)

        self.answerButton = QPushButton()
        self.answerButton.setText("Send")
        self.answerButton.setFont(QFont('Helvetica Neue', 20))
        self.answerButton.setFixedWidth(160)
        self.answerButton.setStyleSheet("QPushButton {"
                                      "background-color: #E4C1F9;"
                                      "padding: 15px; "
                                      "border-style: outset;"
                                      "margin: 10px"
                                      "}"
                                      "QPushButton:pressed {"
                                      "background-color: #A9DEF9;"
                                      "padding:15px;"
                                      "border-style: inset;"
                                      "}")
        self.answerButton.setDisabled(True)
        self.answerButton.setFixedHeight(75)
        self.answerButton.clicked.connect(self.sendAnswer)

        # putting it together
        self.widget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.widget)
        self.mainLayout.addWidget(self.questionLabel)
        self.mainLayout.addWidget(self.tossupLabel)
        self.mainLayout.addWidget(self.answerLabel)

        self.scoreLayout = QHBoxLayout(self.widget)

        self.humanscore = QHBoxLayout(self.widget)
        self.humanscore.addWidget(self.humanTag)
        self.humanscore.addWidget(self.scorehuman)
        self.humanscore.setSpacing(0)

        self.botscore = QHBoxLayout(self.widget)
        self.botscore.addWidget(self.scorebot)
        self.botscore.addWidget(self.botTag)
        self.botscore.setSpacing(0)

        self.scoreLayout.addLayout(self.humanscore)
        self.scoreLayout.addWidget(self.tossupTimer)
        self.scoreLayout.addLayout(self.botscore)
        self.scoreLayout.setSpacing(0)

        self.mainLayout.addLayout(self.scoreLayout)
        self.mainLayout.addWidget(self.statusWindow)
        self.mainLayout.addWidget(self.buzzButton)

        self.answerLayout = QHBoxLayout(self.widget)
        self.answerLayout.addWidget(self.answerBox)
        self.answerLayout.addWidget(self.answerButton)
        self.answerLayout.setSpacing(0)

        self.mainLayout.addLayout(self.answerLayout)
        self.mainLayout.setSpacing(0)
        self.mainLayout.addStretch(1)
        self.setCentralWidget(self.widget)
        self.show()
        self.buzzed = False
        self.buzzLockout = True
        self.currentBuzzResponse = ""
        qApp.processEvents()
        tuthread = threading.Thread(target=self.writeTU)
        tuthread.daemon = True
        tuthread.start()


    def writeTU(self):
        global statusString
        global meScore
        global botScore
        statusString += "Welcome to QuickBuzz Trainer.\nPress spacebar to buzz.\nPress enter to submit your answer\n" \
                             "Good luck!\n" \
                             f"You are facing Bot {botDiff}!\n"
        self.statusWindow.setText(statusString)
        for i in range(0, len(gameTossups)):
            self.buzzLockout = True
            currentTossup = gameTossups[i]
            currentTossupCategory = gameTossupCategories[i]
            currentTossupID = gameTossupIDs[i]
            currentAnswer = gameAnswers[i].split("\n")[0]
            if "[" in currentAnswer:
                currentAnswer = currentAnswer.split("[")[0]
            if "(" in currentAnswer:
                currentAnswer = currentAnswer.split("(")[0]
            if "<" in currentAnswer:
                currentAnswer = currentAnswer.split("(")[0]

            self.tossupLabel.setText(f"Tossup {i+1} - {currentTossupID.split('-')[0]} - {currentTossupCategory}")
            self.answerLabel.setText(f"Answer:")
            currentTossupWords = currentTossup.split(" ")
            if "(*)" not in currentTossup:
                currentTossupWords[len(currentTossupWords)//2] += "(*)"
            currentText = ""
            power = True
            self.buzzLockout = False
            self.buzzed = False
            self.currentBuzzResponse = ""
            statusString += f"Now reading Tossup {i + 1}\n"
            self.statusWindow.setText(statusString)
            qApp.processEvents()
            self.correct = False
            self.negged = False
            self.answerBox.setPlaceholderText("Answer")
            self.tossupTimer.setText("Tossup")
            botWordBuzz = -1
            botNeg = 0
            if botDiff == 1:
                botNeg = random.choices([0,1], [.9, .1])
                botWordBuzz = int(random.uniform(0.95, 0.99)*(len(currentTossupWords)-1))
            elif botDiff == 2:
                botWordBuzz = int(random.uniform(0.8, 0.95)*(len(currentTossupWords)-1))
                botNeg = random.choices([0,1], [.92, .08])
            elif botDiff == 3:
                botWordBuzz = int(random.uniform(0.6, 0.8)*(len(currentTossupWords)-1))
                botNeg = random.choices([0,1], [.95, .05])
            elif botDiff == 4:
                botWordBuzz = int(random.uniform(0.4, 0.6)*(len(currentTossupWords)-1))
                botNeg = random.choices([0,1], [.97, .03])
            elif botDiff == 5:
                botWordBuzz = int(random.uniform(0.2, 0.4)*(len(currentTossupWords)-1))
                botNeg = random.choices([0,1], [.99, .01])
            for j in range(0,len(currentTossupWords)):
                if self.correct:
                    break
                if j == botWordBuzz:
                    botQDepth.append((100*(j+1)/len(currentTossupWords)))
                    statusString += f"Bot {botDiff} buzzed!\n"
                    self.statusWindow.setText(statusString)
                    time.sleep(1)
                    if botNeg == [0]:
                        self.correct = True
                        currentText = currentTossup
                        statusString += f"Bot {botDiff} answered with {currentAnswer}.\n"
                        self.statusWindow.setText(statusString)
                        qApp.processEvents()
                        if power:
                            botScore += 15
                            statusString += f"Bot {botDiff} was correct! For Power! +15 for Bot.\n"

                            self.statusWindow.setText(statusString)
                            qApp.processEvents()
                        else:
                            botScore += 10
                            statusString += f"Bot {botDiff} was correct! +10 for Bot.\n"
                            self.statusWindow.setText(statusString)
                            qApp.processEvents()
                        self.questionLabel.setText(currentText)
                        self.scorehuman.setText(f"{meScore}")
                        self.scorebot.setText(f"{botScore}")
                        qApp.processEvents()
                    else:
                        statusString += f"Bot {botDiff} answered with uhhh.\n"
                        statusString += f"Bot {botDiff} negged! -5 for Bot.\n"
                        botScore -= 5
                        self.statusWindow.setText(statusString)
                        self.scorehuman.setText(f"{meScore}")
                        self.scorebot.setText(f"{botScore}")
                        qApp.processEvents()

                if not self.buzzed:
                    if "(*)" in currentTossupWords[j]:
                        power = False
                    currentText += currentTossupWords[j] + " "
                    if power:
                        self.questionLabel.setStyleSheet("color: red; margin-right: 10px; margin-left: 10px; border: 1px solid black")
                    else:
                        self.questionLabel.setStyleSheet("color: black; margin-right: 10px; margin-left: 10px; border: 1px solid black")
                    self.questionLabel.setText(currentText)
                    qApp.processEvents()
                    time.sleep(0.2)
                else:
                    meQDepth.append((100*(j+1)/len(currentTossupWords)))
                    statusString += "Player buzzed!\n"

                    self.statusWindow.setText(statusString)
                    qApp.processEvents()
                    self.answerSent = False
                    start = time.time()
                    self.answerBox.setDisabled(False)
                    self.answerButton.setDisabled(False)
                    timeup = False
                    while not timeup:
                        end = time.time()
                        if end - start >= 9 or self.answerSent:
                            timeup = True

                    statusString += f"Player answered with {self.answerBox.text().strip()}.\n"
                    self.statusWindow.setText(statusString)
                    if self.answerBox.text().lower().strip() == currentAnswer.lower().strip():
                        currentText = currentTossup
                        self.correct = True
                        if power:
                            meScore += 15
                            statusString += "Player was correct! For Power! +15 for Player.\n"

                            self.statusWindow.setText(statusString)
                            qApp.processEvents()
                        else:
                            meScore += 10
                            statusString += "Player was correct! +10 for Player.\n"

                            self.statusWindow.setText(statusString)
                            qApp.processEvents()
                        self.answerBox.clear()
                        self.questionLabel.setText(currentText)
                        self.scorehuman.setText(f"{meScore}")
                        self.scorebot.setText(f"{botScore}")
                        qApp.processEvents()
                        break
                    else:
                        meScore -= 5
                        statusString += "Player negged! -5 for Player.\n"

                        self.statusWindow.setText(statusString)
                        qApp.processEvents()
                        i-=1
                        self.negged = True
                        self.answerBox.setPlaceholderText("Negged")
                        self.scorehuman.setText(f"{meScore}")
                        self.scorebot.setText(f"{botScore}")
                        qApp.processEvents()
                    self.buzzed = False
                    self.buzzLockout = False
                    self.answerBox.setDisabled(True)
                    self.answerButton.setDisabled(True)
                    qApp.processEvents()

            if not self.correct:
                start = time.time()
                while True:
                    if self.buzzed:
                        meQDepth.append(100)
                        statusString += "Player buzzed!\n"

                        self.statusWindow.setText(statusString)
                        qApp.processEvents()
                        self.answerSent = False
                        astart = time.time()
                        self.answerBox.setDisabled(False)
                        self.answerButton.setDisabled(False)
                        timeup = False
                        while not timeup:
                            aend = time.time()
                            if aend - astart >= 5 or self.answerSent:
                                timeup = True

                        statusString += f"Player answered with {self.answerBox.text().strip()}.\n"
                        self.statusWindow.setText(statusString)

                        if self.answerBox.text().lower().strip() == currentAnswer.lower().strip():
                            currentText = currentTossup
                            self.correct = True
                            if power:
                                meScore += 15
                                statusString += "Player was correct! For Power! +15 for Player.\n"

                                self.statusWindow.setText(statusString)
                                qApp.processEvents()
                            else:
                                meScore += 10
                                statusString += "Player was correct! +10 for Player.\n"

                                self.statusWindow.setText(statusString)
                                qApp.processEvents()
                            self.answerBox.clear()
                            self.questionLabel.setText(currentText)
                            self.scorehuman.setText(f"{meScore}")
                            self.scorebot.setText(f"{botScore}")
                            qApp.processEvents()
                            break
                        else:
                            meScore -= 5
                            statusString += "Player negged! -5 for Player.\n"

                            self.statusWindow.setText(statusString)
                            qApp.processEvents()
                            i -= 1
                            self.negged = True
                            self.answerBox.setPlaceholderText("Negged")

                            self.answerBox.clear()
                            self.scorehuman.setText(f"{meScore}")
                            self.scorebot.setText(f"{botScore}")
                            qApp.processEvents()
                        self.buzzed = False
                        self.buzzLockout = False
                        self.answerBox.setDisabled(True)
                        self.answerButton.setDisabled(True)
                        qApp.processEvents()
                    end = time.time()
                    if end - start >= 3:
                        self.tossupTimer.setText("0")
                        break
                    elif end - start >= 2:
                        self.tossupTimer.setText("1")
                    elif end - start >= 1:
                        self.tossupTimer.setText("2")
                    elif end - start >= 0:
                        self.tossupTimer.setText("3")
                self.buzzLockout = True
            self.answerLabel.setText(f"Answer: {currentAnswer}")
            qApp.processEvents()
            botScoreByTossup.append(botScore)
            meScoreByTossup.append(meScore)
            if len(meQDepth) < i+1:
                meQDepth.append(-1)
            if len(botQDepth) < i+1:
                botQDepth.append(-1)
            time.sleep(3)
            self.buzzLockout = False
        self.writeData()

    def meBuzz(self):
        if not self.buzzLockout and not self.negged:
            self.buzzed = True
            self.buzzLockout = True

    def sendAnswer(self):
        self.answerSent = True

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.meBuzz()
        if event.key() == Qt.Key_Return:
            self.sendAnswer()

    def writeData(self):
        with open(f"GameOf-{time.strftime('%Y%m%d-%H%M%S')}.txt", "w+") as datafile:
            for i in range(0,len(meScoreByTossup)):
                datafile.write(f"At Tossup {i+1}:\n"
                               f"Your Score was: {meScoreByTossup[i]}\n"
                               f"Bot Score was: {botScoreByTossup[i]}\n"
                               f"Your QDepth was: {meQDepth[i]}\n"
                               f"Bot QDepth was: {botQDepth[i]}\n\n")


