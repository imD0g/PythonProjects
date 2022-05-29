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
      inp = input("Enter a number between 1-9: ")
      inp = int(inp)
      if inp >=1 and inp <= 9 and board[inp-1]=="-":
            board[inp-1] = currentPlayer
      else:
            print("Invalid input / Spot already taken")

#check for win - Horizontal
def checkhor(board):
      global winner
      if board[0]==board[1]==board[2] and board[1]!="-":
            winner=board[0]
            return True
      elif board[3]==board[4]==board[5] and board[3]!="-":
            winner=board[3]
            return True
      elif board[6]==board[7]==board[8] and board[6]!="-":
            winner=board[6]
            return True

#check for win - vertical
def checkver(board):
      global winner
      if board[0]==board[3]==board[6] and board[0]!="-":
            winner=board[3]
            return True
      elif board[1]==board[4]==board[7] and board[4]!="-":
            winner=board[4]
            return True
      elif board[2]==board[5]==board[8] and board[5]!="-":
            winner=board[5]
            return True

#check for win - diagonal
def checkdia(board):
      global winner
      if board[0]==board[4]==board[8] and board[0]!="-":
            winner=board[4]
            return True
      elif board[2]==board[4]==board[6] and board[4]!="-":
            winner=board[4]
            return True
     

#check for a tie
def checktie(board):
      if "-"not in board:
            printboard(board)
            print("The game is a tie!")
            gameRunning=False

def checkwin():
      if checkdia(board) or checkhor(board) or checkver(board):
            printboard(board)
            gameRunning=False
            print(f"The winner is {winner}")
            quit()

#switch player
def switchplayer():
      global currentPlayer
      if currentPlayer == "x":
            currentPlayer="O"
      else:
           currentPlayer="x" 



while gameRunning:
      printboard(board)
      playerinput(board)
      checkwin()
      checktie(board)
      switchplayer()
