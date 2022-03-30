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
    elif color == 1:
        pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    elif color == 2:
        pygame.draw.polygon(screen, (255, 0, 0), poly, 0)

def colisionHead(currentX, currentY):

    snake_queue_only_body = snake_queue[:len(snake_queue) - 1]
    if (currentX, currentY) in snake_queue_only_body:
        return True
    else:
        return False

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
move = UP
size = 1
snake_queue = [(currentPositionX-1, currentPositionY),(currentPositionX, currentPositionY)]

# Introducimos punto objetivo
targetX = np.random.randint(0, nxC)
targetY = np.random.randint(0, nyC)

drawPoligon(targetX, targetY, 2)

while currentPositionX < nxC and currentPositionY < nyC \
        and currentPositionX >= 0 and currentPositionY >= 0\
        and not colisionHead(currentPositionX, currentPositionY):

    screen.fill(bg)
    time.sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and move != DOWN:
                move = UP
                break
            elif event.key == pygame.K_d and move != LEFT:
                move = RIGHT
                break
            elif event.key == pygame.K_s and move != UP:
                move = DOWN
                break
            elif event.key == pygame.K_a and move != RIGHT:
                move = LEFT
                break

    if move == UP:
        currentPositionY -= 1
    if move == RIGHT:
        currentPositionX += 1
    if move == DOWN:
        currentPositionY += 1
    if move == LEFT:
        currentPositionX -= 1

    if currentPositionX != targetX or currentPositionY != targetY:
        snake_queue.pop(0)
    else:
        print(snake_queue)
        targetX = np.random.randint(1, nxC-1)
        targetY = np.random.randint(1, nyC-1)

    snake_queue.append((currentPositionX, currentPositionY))

    for snake_body in snake_queue:
        if snake_body == snake_queue[len(snake_queue)-1]:
            drawPoligon(snake_body[0], snake_body[1], 1)
        else:
            drawPoligon(snake_body[0], snake_body[1], 0)

    drawPoligon(targetX, targetY, 2)
    pygame.display.flip()

print("Fin del juego")

# Pulsar tecla para salir
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()


