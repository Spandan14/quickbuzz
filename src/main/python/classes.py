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
                 , "Social Studies Linguistics", "Social Studies Other", "Social Studies Political Science"
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
                self.categoryDrop.setPlaceholderText("Everything")
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
        self.categoryDrop.setPlaceholderText(text)
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
        print(self.gridx)
        print(self.gridy)
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
            if returnValue == QMessageBox.Ok:
                print("ok")


        self.categoryDrop.clear()
        for i in categories:
            if "Everything" in selectedCategories:
                break
            if i not in selectedCategories:
                if i != "Everything":
                    self.categoryDrop.addItem(i)



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
        print(selectedCategories)

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
        if "Everything" in selectedCategories:
            self.subCategoryDrop.addItem("Everything")
        else:
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
            print(temp)
            i = self.subCategoryDrop.count()
            while i >= 0:
                print(self.subCategoryDrop.itemText(i))
                print(i)
                if temp[1] in self.subCategoryDrop.itemText(i):
                    self.subCategoryDrop.removeItem(i)
                    i+=1
                i-=1

        for i in range(self.subCategoryDrop.count()):
            if self.subCategoryDrop.itemText(i) == text:
                self.subCategoryDrop.removeItem(i)

        selectedSubCategories.append(text)

        self.subCategoryDrop.setPlaceholderText(text)

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
        print(self.gridx)
        print(self.gridy)
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
            if returnValue == QMessageBox.Ok:
                print("ok")



    def back(self):
        self.hide()
        self.startwindow = CategorySelection()
        self.startwindow.show()

    def next(self):
        self.hide()
        self.diffwindow = DifficultySelection()
        self.diffwindow.show()
        print(selectedSubCategories)


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
        self.diffDrop.setPlaceholderText(text)
        if "Everything" not in text:
            for i in range(self.diffDrop.count()):
                if "Everything" in self.diffDrop.itemText(i):
                    self.diffDrop.removeItem(i)




        selectedDifficulties.append(text)

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
        print(self.gridx)
        print(self.gridy)
        self.gridy += 1
        if self.gridy % 5 == 0 and self.gridy > 0:
            self.gridx += 1
            self.gridy = self.gridy % 5
        selectedDifficultiesButtons.append(self.tempButton)

    def removeDiff(self):
        try:


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
            catReply.setText("There are no subcategories to remove")
            catReply.setStandardButtons(QMessageBox.Ok)

            returnValue = catReply.exec()
            if returnValue == QMessageBox.Ok:
                print("ok")




    def back(self):
        self.hide()
        self.startwindow = SubCategorySelection()
        self.startwindow.show()

    def next(self):
        self.hide()