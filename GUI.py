import pygame
from control import Board
import copy
pygame.init()

displayh = 400
displayw = 400
window = pygame.display.set_mode((displayh,displayw))
background = (187, 173, 160)
fontSize = 32
fontColor = (0, 0, 0)

pygame.display.set_caption("2048")


class MainRun(object):
    def __init__(self,displayw,displayh):
        self.dw = displayw
        self.dh = displayh
        self.Main()

    def drawBoard(self,board):
        blockSize = self.dw / board.boardSize
        for i in range(board.boardSize):
            for j in range(board.boardSize):
                pygame.draw.rect(window, (222, 222, 222), 
                (j * blockSize, i * blockSize, blockSize, blockSize))
                number = board.board[i][j]
                if number != 0:
                    color = board.getColor(i, j)
                    pygame.draw.rect(window, color, 
                    (j * blockSize + 5, i * blockSize + 5,
                    blockSize - 10, blockSize - 10))

                    font = pygame.font.Font(None, fontSize)
                    text = font.render(str(number), True, fontColor)
                    textWin = text.get_rect(center = 
                    (j * blockSize + blockSize / 2, 
                    i * blockSize + blockSize / 2))
                    window.blit(text, textWin)

    def drawGameover(self):
        pygame.draw.rect(window, background, (0, 0, self.dw, self.dh))
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over!", True, fontColor)
        text_rect = text.get_rect(center=(self.dw / 2, self.dh / 2))
        window.blit(text, text_rect)
        pygame.display.update()
    
    def drawWin(self):
        pygame.draw.rect(window, background, 
                        (0, 0, self.dw, self.dh))
        font = pygame.font.Font(None, 48)
        text = font.render("You Win! O.o", True, fontColor)
        text_rect = text.get_rect(center=(self.dw / 2, self.dh / 2))
        window.blit(text, text_rect)
        pygame.display.update()

    def Main(self):
        #initialization
        board = Board(4, [[]])
        board.empty()
        board.newNumber()
        board.newNumber()
        stopped = False

        while not stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: stopped = True
                elif event.type == pygame.KEYDOWN:
                    #move
                    dir = pygame.key.get_pressed()
                    new = False
                    if dir[pygame.K_DOWN]:
                        tempBoard = copy.deepcopy(board.board)
                        board.moveDown()
                        new = board.boardCheck(tempBoard)
                        if new: board.newNumber()
                    elif dir[pygame.K_UP]:
                        tempBoard = copy.deepcopy(board.board)
                        board.moveUp()
                        new = board.boardCheck(tempBoard)
                        if new: board.newNumber()
                    elif dir[pygame.K_RIGHT]:
                        tempBoard = copy.deepcopy(board.board)
                        board.moveRight()
                        new = board.boardCheck(tempBoard)
                        if new: board.newNumber()
                    elif dir[pygame.K_LEFT]:
                        tempBoard = copy.deepcopy(board.board)
                        board.moveLeft()
                        new = board.boardCheck(tempBoard)
                        if new: board.newNumber()
                    #restart
                    elif dir[pygame.K_r]:
                        board = Board(4, [[]])
                        board.empty()
                        board.newNumber()
                        board.newNumber()
                        stopped = False
                    
                #draw
                self.drawBoard(board)
                pygame.display.update()
                
                #win
                if board.isWin():
                    self.drawWin()
                    if event.type == pygame.QUIT: stopped = True
                    elif event.type == pygame.KEYDOWN:
                        dir = pygame.key.get_pressed()
                        new = False
                        if dir[pygame.K_r]:
                            board = Board(4, [[]])
                            board.empty()
                            board.newNumber()
                            board.newNumber()
                            stopped = False

                #lose 
                if board.isGameOver(): 
                    self.drawGameover()
                    if event.type == pygame.QUIT: stopped = True
                    elif event.type == pygame.KEYDOWN:
                        dir = pygame.key.get_pressed()
                        new = False
                        if dir[pygame.K_r]:
                            board = Board(4, [[]])
                            board.empty()
                            board.newNumber()
                            board.newNumber()
                            stopped = False  

MainRun(displayw, displayh) 
                





    
    


