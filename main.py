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
UP = 771
RIGHT = 2
DOWN = 3
LEFT = 4

# Inicializamos movimiento
# event = pygame.K_w


while True:

    screen.fill(bg)
    time.sleep(0.1)
    drawPoligon(currentPositionX, currentPositionY, 0)

    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.KEYUP:
            if event.type == pygame.KEYUP:
                print("Presionado arriba")
                currentPositionX -= 1
            if event.type == pygame.K_RIGHT:
                print("Presionado derecha")
                currentPositionY += 1
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                print("Presionado izquierda")
                currentPositionX += 1
            if event.type == pygame.KEYDOWN:
                print("Presionado abajo")
                currentPositionY -= 1

    drawPoligon(currentPositionX, currentPositionY, 1)

    pygame.display.flip()


