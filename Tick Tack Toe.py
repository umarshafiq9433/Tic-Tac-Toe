import msvcrt
import os

moves = "123456789"

def getch():
  """
  This function gets a single character from user input without waiting for Enter
  (Windows only).
  """
  return msvcrt.getch().decode('utf-8')

def board():
    os.system('cls')
    board_template = """        Player 1 Symbol: O
        Player 2 Symbol: X
           {} | {} | {}
           ---------
           {} | {} | {}
           ---------
           {} | {} | {}"""
    board_template.center(20,"-")
    formatted_board = board_template.format(*tuple(moves))
    print(formatted_board)

def isDraw():
    totalCounts = moves.count("X") + moves.count("O")
    if totalCounts >= 9 :
        return 0
    else:
        return -1

def winCheck():
    if moves[0] == moves[1] == moves[2]:
        return 1
    elif moves[3] == moves[4] == moves[5]:
        return 1
    elif moves[6] == moves[7] == moves[8]:
        return 1
    elif moves[0] == moves[3] == moves[6]:
        return 1
    elif moves[1] == moves[4] == moves[7]:
        return 1
    elif moves[2] == moves[5] == moves[8]:
        return 1
    elif moves[0] == moves[4] == moves[8]:
        return 1
    elif moves[2] == moves[4] == moves[6]:
        return 1
    else:
        return isDraw()

def isValid(selection):
    if moves.count(selection):
        return 0
    else:
        return 1


def play():
    global moves
    player = 0
    while winCheck()==-1 :
        board()
        player = 1 if player % 2 ==0 else 2
        symbol = 'X' if player % 2 == 0 else 'O'
        playerTurn = "Player: {}"
        print(playerTurn.format(player))
        selection = input("Enter your choice: ")
        if isValid(selection):
            print("Invalid Move!")
            getch()
            player -= 1
            continue
        moves = moves.replace(selection[0], symbol)
    else:
        if winCheck():
            board()
            winMessage = "Player {} won!"
            print(winMessage.format(player))
        else:
            print("Draw!")

play()
