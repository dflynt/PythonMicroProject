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

#Board width and height is taken from command line arguments
#[1] is width
#[2] is height
if int(sys.argv[1]) < 5 or int(sys.argv[2]) < 5:
    print("Heighth and width must be 5 or higher. Exiting program")
    sys.exit()
game = Game(int(sys.argv[1]), int(sys.argv[2]))
game.populateBoard()
game.createBoundaries()
game.printBoard()