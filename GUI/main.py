import pygame
from griglia import GrigliaVuota
from board import Board
import ProblemParse
pygame.init()


SCREEN_WIDTH= 800
SCREEN_HEIGHT = 600


GRID_SIZE = 400

problem = "v3/Problems/rushHour_Problem6X6XY.pddl"
N_GRID = ProblemParse.findBoardDim(problem)

CELL_SIZE = GRID_SIZE/N_GRID

RED = (255,0,0)
WHITE = (255,255,255)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill(WHITE)
#quadrato = pygame.Rect(0,0,GRID_SIZE,GRID_SIZE)
quadratoCentrale = pygame.Rect(screen.get_rect().centerx-GRID_SIZE/2,
                        screen.get_rect().centery-GRID_SIZE/2,
                        GRID_SIZE,GRID_SIZE)
quadratoSchermo = screen.get_rect()


board = Board(problem,screen,quadratoCentrale,CELL_SIZE,N_GRID)
for e in board.vehicles:
    print(e)
#quadratoVuoto = pygame.Rect()

done = False
while not done:
    screen.fill(WHITE)
    clock.tick(2)
    #print(clock.get_fps())
    #pygame.draw.rect(screen,RED,quadrato,2)
    #pygame.draw.rect(screen,RED,quadratoCentrale,2)
    
    #print(GrigliaVuota(quadratoCentrale,2).cellSize)
    GrigliaVuota(quadratoCentrale,N_GRID).drawGriglia(screen)
    board.drawVehicles()

    #quadratoCentrale.left=quadratoCentrale.left+2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(board.getCoord(pygame.mouse.get_pos()))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #print("up")
                board.vehicles[-2].move([7,board.vehicles[-2].coords[0][1]-1])
            



    pygame.display.update()

pygame.quit()