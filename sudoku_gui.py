import pygame
import time
import threading


# Leeres Sudoku-Board (kann vorgefüllt werden)
sudoku = [
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0]
		]

# Ob der Algorithmus in Echtzeit laufen soll oder nicht (Standard: False)
inRealTime = True


WIDTH, HEIGHT = 900, 950
BLACK = (0,0,0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255,0,0)


pygame.init()


class Grid:

    def __init__(self,board,WIN):
        self.board = board
        self.WIN = WIN
        self.cubes = []
        self.selectedCube = None
        for i in range(9):
            for j in range(9):
                cube = Cube(board[i][j],(100*j,100*i),100,WIN,(i,j))
                self.cubes.append(cube)


    def draw_grid(self):
        self.__draw_board()
        for c in self.cubes:
            c.drawNumber()
        if self.selectedCube != None:    
            self.selectedCube.drawRect()

    def __draw_board(self):
        WIN = self.WIN
        WIN.fill(WHITE)

        gap = 0 

        for i in range(10):
            if i%3 == 0 or i==0 or i==9:
                pygame.draw.line(WIN,BLACK,(gap,0),(gap,WIDTH),6)
                pygame.draw.line(WIN,BLACK,(0,gap),(WIDTH,gap),6)
            else:
                pygame.draw.line(WIN,BLACK,(gap,0),(gap,WIDTH),3)
                pygame.draw.line(WIN,BLACK,(0,gap),(WIDTH,gap),3)
            gap += int(WIDTH/9)
    
    def selectCube(self,pos):
        for c in self.cubes:
            if c.posInCube(pos):
                self.selectedCube = c
                return c
        self.selectedCube = None
        return None

    def getCubeByGridPos(self,gridPos):
        for c in self.cubes:
            if c.gridPos == gridPos:
                return c
        return None


class Cube:   

    def __init__(self,number,pos,gap,WIN,gridPos):
        self.number = number
        #if number == 0:
            #self.editable = True
        #else: self.editable = False
        self.editable = True
        self.pos = pos
        self.gap = gap
        self.rect = pygame.Rect(pos,(gap,gap))
        self.font = pygame.font.SysFont("Arial", 90)
        self.WIN = WIN      
        self.gridPos = gridPos 
     
    def posInCube(self,pos):
        if pos[0] > self.pos[0] and pos[0] < (self.pos[0] + self.gap):
            if pos[1] > self.pos[1] and pos[1] < (self.pos[1] + self.gap):   
                return True
        return False

    def drawNumber(self):
        if self.number == 0:
            return
        img = self.font.render(str(self.number), True, GRAY if self.editable else BLACK)
        self.WIN.blit(img, (((self.gap - img.get_rect().width)/2)+self.pos[0], self.pos[1]))

    def drawRect(self):
        pygame.draw.rect(self.WIN,RED,self.rect,6)

    def changeNumber(self,num,isSolver):
        self.number = num
        if not isSolver: 
            sudoku[self.gridPos[0]][self.gridPos[1]] = num
            self.editable = False


def solveSudoku(grid,isRealTime):
    pos = nextEmpty()

    if pos is None:
        grid.WIN.fill(GREEN)
        return True

    for n in range(1,10):
        if isValid(pos,n):
            sudoku[pos[0]][pos[1]] = n

            c = grid.getCubeByGridPos((pos[0],pos[1]))
            c.changeNumber(n,True)
            grid.draw_grid()
            pygame.display.update()
            if not isRealTime: time.sleep(0.05)  

            if solveSudoku(grid,isRealTime):
                return True
            else:
                sudoku[pos[0]][pos[1]] = 0
                c = grid.getCubeByGridPos((pos[0],pos[1]))
                c.changeNumber(0,True)
                grid.draw_grid()
                pygame.display.update()
                if not isRealTime: time.sleep(0.1)  

    return False

def nextEmpty():
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				pos = [i,j]
				return pos
	return None


def isValid(pos,n):
	for i in range(9):
		if (n == sudoku[pos[0]][i] or n == sudoku[i][pos[1]]):
			return False

	l = (pos[0] // 3) * 3
	c = (pos[1] // 3) * 3

	for i in range(l,l+3):
		for j in range(c,c+3):
			if(sudoku[i][j] == n):
				return False
	return True


def main():

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    grid = Grid(sudoku,WIN)

    run = True 
    isSolving = False
    clock = pygame.time.Clock()
    

    while run:
        clock.tick(60)
        grid.draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                c = grid.selectCube(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and not isSolving:
                    print("Backspace")
                    if grid.selectedCube: grid.selectedCube.changeNumber(0,False)
                elif event.key == pygame.K_SPACE and not isSolving:
                    #print("Space")
                    isSolving = True
                    threading._start_new_thread(solveSudoku,(grid,inRealTime))
                elif not isSolving:
                    try:
                        zahl = int(event.unicode)
                        if zahl < 10 and zahl >= 0:
                            grid.selectedCube.changeNumber(zahl,False)
                    except:
                        pass

        pygame.display.update()
        
        
    pygame.quit()


if __name__ == "__main__":
    main()

    


