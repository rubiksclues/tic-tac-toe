# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:49:16 2021
Tic Tac Toe
@author: Courtney
"""
#import
import random


#display gameboard
def display(board):
    print('|'+ board[7] + '|'+ board[8] +'|'+board[9] + '|')
    print('|'+ board[4] + '|' + board[5] +'|' +board[6] + '|')
    print('|'+ board[1] + '|'+ board[2] + '|'+board[3] + '|')
    

#player chooses X or O
def user_input():
    '''
    returns tuple of player inputs as: player1, player2
    '''
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    


#position player input onto board
def position_marker(board,marker,position):
    board[position] = marker
    
    return board

#check if the mark has won, if there is a tie, or if the game is ongoing
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal  
    

#function decides which player goes first
def choose_first():
    players = ('player 1', 'player 2')
    return random.choice(players)

#checks if board space is free
def space_check(board, position):
    return board[position] == ' '

#checks if board is full indicating a tie
def full_board_check(board):
    for i in range (1,10):
        if space_check(board,i):
            return False
    return True

#checks if players choice is a free position
def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position: '))
        
    return position

#function for if the player wants to play again
def play_again():
    choice = ''
    
    while choice not in ['Y', 'N']:
        choice = input('Would you like to play again? (Y/N): ')
        
        if choice not in ['Y', 'N']:
            print('Please choose a valid option, (Y/N): ')
            
    if choice == 'Y':
        return True
    if choice == 'N':
        return False
    

print('---WELCOME TO TIC TAC TOE---')

while True:
    #game board
    board = [' '] * 10
    player1_marker, player2_marker = user_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play = input('Are you ready to begin tic tac toe? (Y/N): ')
    
    if play == 'Y':
        tictactoe = True
    if play == 'N':
        tictactoe = False
        
    while tictactoe:
        
        if turn == 'player 1':
            display(board)
            position = player_choice(board)
            position_marker(board, player1_marker, position)
            
            if win_check(board, player1_marker):
                display(board)
                print('Congrats! You won!')
                tictactoe = False
            else:
                if full_board_check(board):
                    display(board)
                    print('It is a draw!')
                    break
                else:
                    turn == 'player 2'
                
        else:
            display(board)
            position = player_choice(board)
            position_marker(board, player2_marker, position)
            
            if win_check(board, player2_marker):
                display(board)
                print('Congrats! You won!')
                tictactoe = False
            else:
                if full_board_check(board):
                    display(board)
                    print('It is a draw!')
                    break
                else:
                    turn = 'player 1'
                    
    if not play_again():
        break 
    
    
    
    
    


        

