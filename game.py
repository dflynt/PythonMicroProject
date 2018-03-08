import sys

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height
        self.board = []

    def populateBoard(self):
        for i in range(0, self.width):
            self.board.append([])
            for l in range(0, self.height):
                if l == 0 or l == self.width - 1: #top and bottom row boundaries
                    self.board[i].append(" 0 ")
                elif i == 0 or i == self.height - 1: #first and last column boundaries
                    self.board[i].append(" 0 ")
                else:
                    self.board[i].append(" 1 ")

        # hard code entry and exit
        # line 23 = exit
        # line 25 = entry           
        self.board[0][self.width - 2] = " 1 "
        self.board[self.height - 1][1] = " 1 "

    # hard code boundaries
    def createBoundaries(self):
        for x in range(2,6):
            self.board[2][x] = " 0 "
        for x in range(3, 7):
            self.board[5][x] = " 0 "
        
    def printBoard(self):
        for line in range(0, self.width):
              print(' '.join(self.board[line])) #.join on space removes brackets, commas, and quotes when printing lists

    def getheight(self):
        return self.height

    def getwidth(self):
        return self.width

    def getboard(self):
        return self.board

    def setboard(self, board):
        self.board = board

#Board width and height is taken from command line arguments
#[1] is width
#[2] is height
print(sys.argv[1])
print(sys.argv[2])
game = Game(int(sys.argv[1]), int(sys.argv[2]))
game.populateBoard()
game.createBoundaries()



'''
Game logic starts here.
'''
playing = True
playerposition = game.getboard()
x = game.getheight() - 1
y = 1
playerposition[x][y] = " 2 "

game.setboard(playerposition)
game.printBoard()

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
        if  x - 1 < game.getwidth() and playerposition[x - 1][y] != " 0 ":
            playerposition[x][y] = " 1 "
            x -= 1
            playerposition[x][y] = " 2 "
    # move down
    elif event == "s" or event == "S":
        if x + 1 < game.getwidth() and playerposition[x + 1][y] != " 0 ":
            playerposition[x][y] = " 1 "
            x += 1
            playerposition[x][y] = " 2 "
    # move right
    elif event == "d" or event == "D":
        if y + 1 < game.getheight() and playerposition[x][y + 1] != " 0 ":
            playerposition[x][y] = " 1 "
            y += 1
            playerposition[x][y] = " 2 "
    # move left
    elif event == "a" or event == "A":
        if y - 1 < game.getheight() and playerposition[x][y - 1] != " 0 ":
            playerposition[x][y] = " 1 "
            y -= 1
            playerposition[x][y] = " 2 "
    else:
        print("Invalid key. Use WASD only.")

# game is running here
while (playing):
    playermovement(input("Move to? "))
    game.setboard(playerposition)
    game.printBoard()

print("Congrats!")