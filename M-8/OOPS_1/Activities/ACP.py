import pygame 
import sys

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Robot Demo')

WHITE = (255, 255, 255)
RED = (255, 0, 0)

position = [400, 300]
size = 50
speed = 5

active = True
while active:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        position[0] -= speed
    if pressed[pygame.K_RIGHT]:
        position[0] += speed
    if pressed[pygame.K_UP]:
        position[1] -= speed
    if pressed[pygame.K_DOWN]:
        position[1] += speed

    win.fill(WHITE)
    pygame.draw.rect(win, RED, (*position, size, size))
    pygame.display.update()
    pygame.time.Clock().tick(30)
