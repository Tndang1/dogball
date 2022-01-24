import pygame
import random

class Ball:
    def __init__(self, cb_game):
        self.screen = cb_game.screen
        self.screen_rect = cb_game.screen.get_rect()
        self.img = pygame.image.load("imgs/ball.png")
        self.img = pygame.transform.scale(self.img, (15,15))
        self.rect = self.img.get_rect()
        self.vel = 1
        self.direction = random.randint(1,4)
        #create a seperate method?
        if self.direction == 1:
            self.x = random.randint(0, 465)
            self.y = -15
        elif self.direction == 2:
            self.x = random.randint(0, 465)
            self.y = 480
        elif self.direction == 3:
            self.x = -15
            self.y = random.randint(0, 465)
        elif self.direction == 4:
            self.x = 480
            self.y = random.randint(0, 465)

    def moving(self):
        if self.direction == 1:
            self.y += self.vel
        if self.direction == 2:
            self.y -= self.vel
        if self.direction == 3:
            self.x += self.vel
        if self.direction == 4:
            self.x -= self.vel
        self.blit_ball()

    def blit_ball(self):
        self.screen.blit(self.img, self.rect)
