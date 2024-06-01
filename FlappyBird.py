import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

font = pygame.font.SysFont('Bauhaus 93', 60)

bg = pygame.image.load('img/bg.png')
ground = pygame.image.load('img/ground.png')

ground_scroll = 0
pipe_gap = 150
scroll_speed = 4
pipe_frequency = 1500

run = True

while run:
    
    clock.tick(fps)

    screen.blit(bg, (0, 0))
    screen.blit(ground, (ground_scroll, 768))

    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

pygame.quit
