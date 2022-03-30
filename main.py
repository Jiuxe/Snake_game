import pygame
import numpy as np
import time

# Funciones necesarias para implementacion

def drawPoligon(x, y, color):
    poly = [((x) * dimCW, y * dimCH),
            ((x + 1) * dimCW, y * dimCH),
            ((x + 1) * dimCW, (y + 1) * dimCH),
            ((x) * dimCW, (y + 1) * dimCH)]

    if color == 0:
        pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
    else:
        pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

# ---------------------------------------------- #

pygame.init()

width, height = 500, 500

screen = pygame.display.set_mode((width,height))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

# Posicion inicial
currentPositionX = nxC // 2
currentPositionY = nyC // 2

# Direcciones
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

# Inicializamos movimiento
move = 1


while currentPositionX < nxC and currentPositionY < nyC and currentPositionX > 0 and currentPositionY > 0:

    screen.fill(bg)
    time.sleep(0.1)
    drawPoligon(currentPositionX, currentPositionY, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and move != DOWN:
                move = UP
            if event.key == pygame.K_d and move != LEFT:
                move = RIGHT
            if event.key == pygame.K_s and move != UP:
                move = DOWN
            if event.key == pygame.K_a and move != RIGHT:
                move = LEFT

    if move == UP:
        currentPositionY -= 1
    if move == RIGHT:
        currentPositionX += 1
    if move == DOWN:
        currentPositionY += 1
    if move == LEFT:
        currentPositionX -= 1

    drawPoligon(currentPositionX, currentPositionY, 1)

    pygame.display.flip()

print("Fin del juego")

# pulsar tecla para salir
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

