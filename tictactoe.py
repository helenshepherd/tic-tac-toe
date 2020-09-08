from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+'|'+ board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+ board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+ board[8]+'|'+board[9])

def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    if board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    if board[4]==mark and board[5]==mark and board[6]==mark:
        return True
    if board[7]==mark and board[8]==mark and board[8]==mark:
        return True
    if board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    if board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    if board[3]==mark and board[6]==mark and board[9]==mark:
        return True
    if board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    if board[3]==mark and board[5]==mark and board[7]==mark:
        return True
    else:
        return False

import random

def choose_first():
    randomanswer = random.randint(0,1)
    if randomanswer == 0:
        return 'Player 1 goes first'
    if randomanswer == 1:
        return 'Player 2 goes first'

def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False

def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True

def player_choice(board):
    choice_is_valid = False
    
    while not choice_is_valid:
        choice = input('Please choose a position from 1-9: ')
        if choice.isdigit()==False:
            clear_output()
            display_board(board)
            print("Sorry, I don't understand. Please choose a position from 1-9.")
        elif int(choice) not in range(1,10):
            clear_output()
            display_board(board)
            print("Sorry, I don't understand. Please choose a position from 1-9.")
        elif space_check(board,int(choice))==False:
            clear_output()
            display_board(board)
            print("Sorry, that position is taken. Please choose another.")
        else:
            return int(choice)

    
def replay():
    replaychoice = 'wrong'
    
    while replaychoice not in ['Y','N']:
        replaychoice = input('Do you want to play again? (Y or N): ')
        if replaychoice not in ['Y','N']:
            print("Sorry, I don't understand, please choose Y or N")
    
    if replaychoice == 'Y':
        return True
    else:
        return False

def player_1_turn():
    
    display_board(board)
    print("Player 1's turn")
    position_choice = player_choice(board)
    place_marker(board, player1_marker, position_choice)
    
    if win_check(board, player1_marker)==True:
        display_board(board)
        print('Congratulations! You win!')
        return False
        
    elif full_board_check(board)==True:
        display_board(board)
        print('Game Over!')
        return False
    
    return True

def player_2_turn():

    display_board(board)
    print("Player 2's turn") 
    position_choice = player_choice(board)
    place_marker(board, player2_marker, position_choice)
    
    if win_check(board, player2_marker)==True: 
        display_board(board)
        print('Congratulations! You win!')
        return False
           
    elif full_board_check(board)==True:
        display_board(board)
        print('Game Over!')
        return False
        
    return True
    
import time

game_play = True

while game_play: 
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_on = True
    print('Welcome to Tic Tac Toe!')
    display_board(board)
    player1_marker, player2_marker = player_input()
    
    whose_first = choose_first()
    print(whose_first)
    time.sleep(4)

    if whose_first=='Player 1 goes first':
        is_player_1_turn = True
    else:
        is_player_1_turn = False


    while game_on:
        if is_player_1_turn:
            game_on = player_1_turn()
        else:
            game_on = player_2_turn()
        is_player_1_turn = not is_player_1_turn

    game_play = replay()




