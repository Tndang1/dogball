# imports
from ctypes import sizeof
import sys
import pygame
import random

from player import Player
from ball import Ball

test = False

class CatchBall:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480, 480))
        self.background = pygame.image.load("imgs/game_fill.png")
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.ball_timer = 3000
        self.score = 0
        #Accounts for first ball
        self.possible_score = 1
        self.ball = Ball(self)
        self.balls = [self.ball]
        self.player = Player(self)
        if test:
            self.player.img = pygame.transform.scale(self.player.img, (480, 480))
            self.player.rect = self.player.img.get_rect()
        self.smallfont = pygame.font.Font(None, 24)

    def run_game(self):
        while True:
            self.check_keys()
            self.player.moving()
            if self.possible_score != 50:
                self.ball_timer -= random.randint(0,200)
                if test:
                    self.ball_timer = 0
            if self.ball_timer <= 0:
                #Adds a ball to array if there are no more than 10 on screen
                if len(self.balls) <= 10:
                    self.summon_balls()
                    self.ball_timer = 5000
            for ball in self.balls:
                #Creates rect for each ball in it's current position
                ball_rect = ball.rect
                ball_rect.left = ball.x
                ball_rect.top = ball.y
                #When ball exits screen, removes from array
                if ball.y <= -31 or ball.y >= 481 or ball.x <= -31 or ball.x >= 481:
                    self.balls.pop(self.balls.index(ball))
            self.catch_ball()
            self.update_screen()
            #Limits the framerate
            self.clock.tick(self.fps)

    def check_keys(self):
        for event in pygame.event.get():
            #Allows to exit program by closing the window
            if event.type == pygame.QUIT:
                sys.exit()
            #Begins movement of player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.right = True
                if event.key == pygame.K_a:
                    self.player.left = True
                if event.key == pygame.K_s:
                    self.player.down = True
                if event.key == pygame.K_w:
                    self.player.up = True
                #Exit program by pressing escape key
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            #Stops movement of player
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.right = False
                if event.key == pygame.K_a:
                    self.player.left = False
                if event.key == pygame.K_s:
                    self.player.down = False
                if event.key == pygame.K_w:
                    self.player.up = False
    def update_screen(self):
        #Updates screen with new positions
        self.screen.fill(0)
        self.screen.blit(self.background, (0, 0))
        for ball in self.balls:
            ball.moving()
            #ball.blit_ball()
        self.player.blit_player()
        self.showtext()
        pygame.display.flip()

    def summon_balls(self):
        #Creates ball obejct, adds to array, counts total number of balls created
        if test:
            print("In summon_balls")
        self.possible_score += 1
        ball = Ball(self)
        self.balls.append(ball)

    def catch_ball(self):
        #When player and ball rectangle collide, adds 1 to score and removes ball from array and screen
        for ball in self.balls:
            if ball.rect.colliderect(self.player.rect):
                self.balls.pop(self.balls.index(ball))
                self.score += 1

    def showtext(self):
        text = self.smallfont.render("Caught: " + str(self.score) + " out of: " + str(self.possible_score), True, (255, 255, 255))
        textrect = self.screen.get_rect().topleft
        self.screen.blit(text, textrect)

if __name__ == '__main__':
    if test:
            print("In __main__")
    cb = CatchBall()
    cb.run_game()
