#See if I can do this...
import pandas as pd
import sys
import random
import numpy as np
from sklearn.tree import DecisionTreeRegressor

data_path = 'C:/Users/Kevin/.atom/storage/c4_data2.csv'
game_data = pd.read_csv(data_path)
game_data = game_data.dropna(axis=0)

#Figures out what the highest value is and returns it (assumes the COM player is 1, NOT -1)
def determine_move(pnum, values):
    options = 0
    columns = 7
    best_col = -1
    best_number = 0
    for options in range(0,columns):
        #print(options, values[options])
        if values[options] < best_number and options > 0:
            best_number = values[options]
            best_col = options
        options+=1
    if best_col <= 0:
        best_col = random.randint(0,6)
    return best_col+1

def get_space(column):

    space_number = 35-column_checkers[column-1]*7+column
    column_checkers[column-1]+=1
    return space_number

def update_inputs(player_move, turn):
    #Step 1: Update inputcols
    adjusted = ""
    index = player_move-1
    space_number = 35-column_checkers[index]*7+player_move
    if space_number < 10:
        adjusted = '0'
    inputcols.append('pos_'+adjusted+str(space_number))

    #Step 2: Update board array
    column_checkers[index] += 1
    board[0].append(turn)

    #Step 3: Update y data (Not working)
    update_ydata(player_move, inputcols)
    #print(inputcols)
    #print(column_checkers)
    #print(board)

def calculate_next_move(input, board, column_checkers):
    #Prediction target is...not who's going to win, but the next column that should be played
    #y1 thru y7 are all of the open columns
    #Step 1: Update inputcols
    options = 0
    space_number = 0
    strings = list()
    for options in range(0,7):
        adjusted = ""
        space_number = 36-column_checkers[options]*7+options
        if space_number < 0:
            space_number+=7
        if space_number == 0:
            space_number+=7
        if space_number < 10:
            adjusted = '0'
        strings.append('pos_'+adjusted+str(space_number))
        print(strings[options])

    y1 = getattr(game_data,strings[0])
    y2 = getattr(game_data,strings[1])
    y3 = getattr(game_data,strings[2])
    y4 = getattr(game_data,strings[3])
    y5 = getattr(game_data,strings[4])
    y6 = getattr(game_data,strings[5])
    y7 = getattr(game_data,strings[6])

    x = game_data[input]
    model1 = DecisionTreeRegressor()
    model1.fit(x,y1)
    model2 = DecisionTreeRegressor()
    model2.fit(x,y2)
    model3 = DecisionTreeRegressor()
    model3.fit(x,y3)
    model4 = DecisionTreeRegressor()
    model4.fit(x,y4)
    model5 = DecisionTreeRegressor()
    model5.fit(x,y5)
    model6 = DecisionTreeRegressor()
    model6.fit(x,y6)
    model7 = DecisionTreeRegressor()
    model7.fit(x,y7)

    next_move1 = model1.predict(board)
    next_move2 = model2.predict(board)
    next_move3 = model3.predict(board)
    next_move4 = model4.predict(board)
    next_move5 = model5.predict(board)
    next_move6 = model6.predict(board)
    next_move7 = model7.predict(board)
    columns = [next_move1, next_move2, next_move3, next_move4, next_move5, next_move6, next_move7]
    return columns

def update_ydata(column, input):
    input = game_data[input]
    space_number = 35-column_checkers[column-1]*7+column
    word = 'pos_'+str(space_number)

#This current lineup assumes Red (-1) went first
#inputcols = ['winner', 'pos_36', 'pos_37', 'pos_38', 'pos_39', 'pos_40', 'pos_41', 'pos_42']
column_checkers = [0,0,0,0,0,0,0]
inputcols = ['winner']
board = [[-1]] #AI is black
while 1:
    first_turn = int(input('What column will you play? Enter a value from 1-7     '))
    update_inputs(first_turn,1)

    best_move = determine_move(1,calculate_next_move(inputcols, board, column_checkers))
    print(int(best_move),' was played')
    update_inputs(best_move,-1)




#inputcols = ['winner', 'pos_36', 'pos_37', 'pos_38', 'pos_39', 'pos_40', 'pos_41', 'pos_42','pos_33'
#,
#, 'pos_31', 'pos_32', 'pos_30', 'pos_33','pos_23', 'pos_34'
#]

#    board = [[1, #AI PLayer ID
#    1,1,1,-1,-1,-1, 1,-1   #Row 1
#    ,]]
