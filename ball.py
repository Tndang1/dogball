import pygame
import random

class Ball:
    def __init__(self, cb_game):
        self.screen = cb_game.screen
        self.screen_width = cb_game.screen_width
        self.screen_height = cb_game.screen_height
        self.ball_width = 15
        self.ball_height = 15
        self.screen_rect = cb_game.screen.get_rect()
        self.img = pygame.image.load("imgs/ball.png")
        self.img = pygame.transform.scale(self.img, (self.ball_width, self.ball_height))
        self.rect = self.img.get_rect()
        self.vel = 1
        #Determine starting location of the ball. (0,0) is the top left of the game screen
        self.direction = random.randint(1,4)
        if self.direction == 1:
            #subtracting ball width from screen width ensures ball will appear on the screen
            self.x = random.randint(0, self.screen_width-self.ball_width)
            self.y = (0-self.ball_height)
        elif self.direction == 2:
            self.x = random.randint(0, self.screen_width-self.ball_width)
            self.y = self.screen_height
        elif self.direction == 3:
            self.x = (0-self.ball_width)
            self.y = random.randint(0, self.screen_height-self.ball_height)
        elif self.direction == 4:
            self.x = self.screen_width
            self.y = random.randint(0, self.screen_height-self.ball_height)

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
