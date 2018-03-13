import sys
import random
import os

# The following is the game object.
# This contains the board to move across, the ability to print the board,
# the assurance of proper boundaries and entry/exit points, enemy
# population (no longer implemented), and the ability to alter the board.


class Game:

    # The following code block defines the major parts of the game object,
    # mainly the board itself and its properties.
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height
        self.board = []

    def populateboard(self):
        for i in range(0, self.width):
            self.board.append([])
            for l in range(0, self.height):
                if l == 0 or l == self.width - 1:
                    # top and bottom row boundaries
                    self.board[i].append(" 0 ")
                elif i == 0 or i == self.height - 1:
                    # first and last column boundaries
                    self.board[i].append(" 0 ")
                else:
                    self.board[i].append(" 1 ")

        # hard code entry and exit
        # line 23 = exit
        # line 25 = entry
        self.board[0][self.width - 2] = " 1 "
        self.board[self.height - 1][1] = " 1 "

    # randomize the walls in the maze
    def createboundaries(self):
        for i in range(1, 8):
            self.board[i][random.randint(2,4)] = " 0 "
            self.board[i][random.randint(3, 5)] = " 0 "
            self.board[i][random.randint(6, 8)] = " 0 "

    def printboard(self):
        for line in range(0, self.width):
            print(' '.join(self.board[line]))
            # .join on space removes brackets, commas,
            # and quotes when printing lists

    def getheight(self):
        return self.height

    def getwidth(self):
        return self.width

    def getboard(self):
        return self.board

    def setboard(self, board):
        self.board = board

    def getrandomspace(self, low, high):
        return random.randrange(low, high)

    # '#' character denotes enemy
    # def populateenemies(self, count):
    #     for x in range(0, count):
    #         randWidth = self.getrandomspace(1, self.width - 1)
    #         randHeight = self.getrandomspace(1, self.height - 1)
    #         self.board[randHeight][randWidth] = " # "


game = Game(10, 10)

game.populateboard()
# game.populateenemies(5)
game.createboundaries()

'''
Game logic starts here.
'''
playing = True
playerposition = game.getboard()
x = game.getheight() - 1
y = 1
playerposition[x][y] = " 2 "

game.setboard(playerposition)
game.printboard()

finish_height = 0
finish_width = game.getwidth() - 2


def playermovement(event):
    global y
    global x
    global playing

    # if user makes it to the end
    if y == finish_width and x == finish_height:
        playing = False

    # move up
    if event == "w" or event == "W":
        if x - 1 < game.getwidth() and playerposition[x - 1][y] != " 0 ":
            playerposition[x][y] = " 1 "
            x -= 1
            playerposition[x][y] = " 2 "
        else:
            print ("Invalid move. Try again.")
    # move down
    elif event == "s" or event == "S":
        if x + 1 < game.getwidth() and playerposition[x + 1][y] != " 0 ":
            playerposition[x][y] = " 1 "
            x += 1
            playerposition[x][y] = " 2 "
        else:
            print ("Invalid move. Try again.")
    # move right
    elif event == "d" or event == "D":
        if y + 1 < game.getheight() and playerposition[x][y + 1] != " 0 ":
            playerposition[x][y] = " 1 "
            y += 1
            playerposition[x][y] = " 2 "
        else:
            print ("Invalid move. Try again.")
    # move left
    elif event == "a" or event == "A":
        if y - 1 < game.getheight() and playerposition[x][y - 1] != " 0 ":
            playerposition[x][y] = " 1 "
            y -= 1
            playerposition[x][y] = " 2 "
        else:
            print ("Invalid move. Try again.")
    else:
        print("Invalid key. Use WASD only.")

# game is running here
while (playing):
    playermovement(input("Move to? "))
    game.setboard(playerposition)
    os.system("cls")
    game.printboard()

print("Congrats!")
