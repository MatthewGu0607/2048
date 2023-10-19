import random

def twoOrFour():
    number = random.randint(1,100)
    if number > 30:
        return 512
    else:
        return 512

class Board(object):
    def __init__(self, boardSize, board):
        self.boardSize = boardSize
        self.board = board

    def empty(self):
        self.board = [[0] * self.boardSize for i in range(self.boardSize)]

    def getColor(self,row,col):
        blockColors = {0: (222, 222, 222), 2: (255, 221, 147), 
                       4: (255, 234, 165), 8: (255, 238, 189), 
                       16:(249, 255, 193), 32:(201, 244, 219), 
                       64: (168, 237, 238), 128: (154, 220, 245), 
                       256: (156, 198, 244), 512: (122, 173, 255), 
                       1024: (160, 165, 255), 2048: (140, 137, 244),
        }
        return blockColors.get(self.board[row][col])

    def moveLeft(self):
        for i in range(self.boardSize):
            curRow = []
            zero = 0
            for j in range(self.boardSize):
                if self.board[i][j] == 0:
                    zero += 1
                else:
                    curRow.append(self.board[i][j])
            prev = -1
            row = []
            merge = False
            for col in curRow:
                if not merge and prev == col:
                    merge = True
                    row.append(2 * row.pop())
                    zero += 1
                else:
                    merge = False
                    row.append(col)
                    prev = col
            for number in range(zero):
                row.append(0)
            self.board[i] = row

    def moveUp(self):
        self.board = [list(row) for row in zip(*self.board)]
        self.moveLeft()
        self.board = [list(row) for row in zip(*self.board)]

    def moveRight(self):
        for i in range(self.boardSize):
            self.board[i].reverse()
        self.moveLeft()
        for i in range(self.boardSize):
            self.board[i].reverse()

    def moveDown(self):
        self.board = [list(row) for row in zip(*self.board)]
        self.moveRight()
        self.board = [list(row) for row in zip(*self.board)]

    def newNumber(self):
        empty=[]
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j] == 0:
                    empty.append((i,j))
        (row,col) = random.choice(empty)
        self.board[row][col] = twoOrFour()

    def isWin(self):
        for row in self.board:
            for col in row:
                if col == 2048:
                    return True
        return False
    
    def isGameOver(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j] == 0:
                    return False
                if (( i + 1 < self.boardSize and
                self.board[i][j] == self.board[i + 1][j]) 
                or 
                 (j + 1 < self.boardSize and 
                 self.board[i][j] == self.board[i][j + 1]
                 )):
                 return False
        return True

    def boardCheck(self,board2):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if not self.board[i][j] == board2[i][j]:
                    return True
        return False
