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
flying = False
game_over = False

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
            
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
        
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.counter += 1
            flap_cooldown = 5
        
            if(self.counter > flap_cooldown):
                self.counter = 0
                self.index += 1
                if(self.index >= len(self.images)):
                    self.index = 0
            self.image = self.images[self.index]
        
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
   
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        # position 1 is from top and -1 is from bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y]
        if position == -1:
            self.rect.topleft = [x, y]


bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()


flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)

btm_pipe = Pipe(300, int(screen_height / 2), - 1)
top_pipe = Pipe(300, int(screen_height / 2), 1)
pipe_group.add(btm_pipe)
pipe_group.add(top_pipe)

run = True
while run:
    
    clock.tick(fps)

    screen.blit(bg, (0, 0))

    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    pipe_group.update()

    screen.blit(ground, (ground_scroll, 768))

    if flappy.rect.bottom > 768:
        game_over = True
        flying = False

    if game_over == False:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
            
    pygame.display.update()

pygame.quit
