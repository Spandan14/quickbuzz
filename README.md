# QuickBuzz
## What is QuickBuzz
QuickBuzz is a **dynamic quizbowl/scholastic bowl** training application. QuickBuzz has over *94000 tossups* taken from the [QuizDB](https://www.quizdb.org) database. You can train against a bot which has *5* different skill levels and also save the data of your game for further analysis. This app can be used **offline**, so it is perfect for practice at home and on the go as well!
## Installation Method
To install QuickBuzz, you will need some dependencies
### Dependencies
  * Python 3.8
    * To install, go to the [Python downloads](https://www.python.org/downloads/)
  * PyQt5
    * To install, look at [this page](https://pypi.org/project/PyQt5/)
  * requests and tqdm (optional, only if you plan to redownload QuizDB Database, which is **not recommended**)
  * A brain (**highly recommended**)
### Steps
#### Step 1
Clone the github repository and extract the files to a place you like.
#### Step 2
Navigate to src/main/python
#### Step 3
Run the main.py file using an IDE of choice, or simply by typing `python main.py`. You may need to change `python` accordingly based on your operating system and install configuration.
#### Step 4
Start training with QuickBuzz!
## Usage
### Selecting categories, subcategories, and difficulties
You can select multiple of these. Simply use the dropdown to add them. You should see a small button like widget pop up on the screen. This lets you know that you have selected the right category/subcategory/difficulty. To remove the last added option, use the button above the dropdown.
### Looking for tossups
Press the look for tossups button to find tossups to play with that meet your requirements. **Note: if QuickBuzz shows 0 Tossups available, please exit the application and use different settings. It is rare for this to happen as the databse is rather large, but this will cause the app to not function properly**
### Selecting a Bot
There are 5 Bots in the application you can play with
#### I'm too immature to lose
This is by far the easiest bot. This bot answers the question with a depth of 95 to 99 percent, and has a negrate of 10 percent.
#### Noob
This is another relatively easy bot. This bot answers the question with a depth of 80 to 95 percent, and has a negrate of 8 percent.
#### Mediocre
This is a medium difficulty bot. This bot answers the question with a depth of 60 to 80 percent, and has a negrate of 5 percent. This bot occasionally powers.
#### Captain
This is a hard bot. This bot was made to represent the captain of an average team. This bot answers the question with a depth of 40 to 60 percent, and has a negrate of 3 percent. This bot powers regularly.
#### Pro
This is an extremely hard bot. This bot was made to represent some of the best players in the world. This bot answers the question with a depth of 20 to 40 percent, and has a negrate of 1 percent. This bot powers nearly every time.
### Scoring
Scoring is standard. -5 for a neg, 15 for power, and 10 for all other correct buzzes.
### Interpreting Results
In the master directory, which also has the src directory, you will find the GameOf files. These files are generated upon the completion of a game. They will show you the score by tossup and also the depth for that tossup. If depth is shown as -1, this means that the player did not buzz.
## Final Words
I hope you have a good experience with the application. As of right now, the code is not fully documented as I do not expect anyone to develop/modify this game. If you want to look into some modifications and need some guidance on the code, email spagoel22@students.d125.org
As always, if there are any bugs, feel free to file an issue, and a pull request if you have any changes you would like to propose.
Thank you, and happy training!
