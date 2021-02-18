# ConnectFourML
A Python script utilizing the sklearn library to play Connect Four.

This script uses a DecisionTreeRegressor from SKLearn to determine the optimal moves when playing Connect Four. The model inputs are all spaces occupied by checkers and the predicted winner of the game and is fit to the lowest empty space in each column. The model then predicts the value of the next checker played if player x won, with -1 being the AI and +1 being the human player. The script then compares all seven values and plays a checker with the highest value (most negative if AI player value is -1) and updates its array containing all of the game's inputs.

For a tutorial on using the DecisionTreeRegressor, see: https://www.kaggle.com/dansbecker/how-models-work. This Kaggle course formed the basis for this project.

The dataset utilized can be found at this link: https://www.kaggle.com/tbrewer/connect-4

Note that this script does NOT allow you to play ConnectFour. You will need a game board or app to use this properly.
