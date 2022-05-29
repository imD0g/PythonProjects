from tkinter import N


board=["-", "-", "-",
      "-", "-", "-",
      "-", "-", "-"]
currentPlayer = "x"
winner = None
gameRunning = True

#display board
def printboard(board):
      print("-------------")
      print("| "+board[0] + " | "+board[1]+" | "+board[2]+" |")
      print("-------------")
      print("| "+board[3] + " | "+board[4]+" | "+board[5]+" |")
      print("-------------")
      print("| "+board[6] + " | "+board[7]+" | "+board[8]+" |")
      print("-------------")
print(printboard(board))

# get the user to input 1-9
def playerinput(board):
      inp = int(input("Enter a number between 1-9: "))
      if inp >=1 and inp <= 9 and board[inp-1]=="-":
            board[inp-1] = currentPlayer
      else:
            print("Invalid input / Spot already taken")



while gameRunning:
      printboard(board)
      playerinput(board)

