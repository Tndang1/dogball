# imports
import sys
import pygame
import random

from player import Player
from ball import Ball
from power_ball import PowerBall

_test = False

class CatchBall:
    def __init__(self):
        pygame.init()
        self.screen_width = 560
        self.screen_height = 560
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background = pygame.image.load("imgs/game_fill.png")
        self.clock = pygame.time.Clock()
        self.fps = 120
        self.ball_timer = 3000
        self.score = 0
        #Accounts for first ball
        self.ball_counter = 1
        self.ball = Ball(self)
        self.balls = [self.ball]
        self.player = Player(self)
        if _test:
            self.player.img = pygame.transform.scale(self.player.img, (self.screen_width, self.screen_height))
            self.player.rect = self.player.img.get_rect()
        self.smallfont = pygame.font.Font(None, 24)

    def run_game(self):
        while True:
            self.check_keys()
            self.player.moving()
            if self.ball_counter != 50:
                self.ball_timer -= random.randint(0,200)
                if _test:
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
                if ball.y <= -ball.ball_height-1 or ball.y >= self.screen_height+1 or ball.x <= -ball.ball_width-1 or ball.x >= self.screen_width+1:
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
                if _test:
                    print("Key down recognized")
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
        self.player.blit_player()
        self.showtext()
        pygame.display.flip()

    def summon_balls(self):
        #Creates ball obejct, adds to array, counts total number of balls created
        self.ball_counter += 1
        ball_chance = random.randint(1, 10)
        if ball_chance > 8:
            ball = PowerBall(self)
            ball.vel = random.uniform(1.5, 2.5)
        else:
            ball = Ball(self)
        self.balls.append(ball)

    def catch_ball(self):
        #When player and ball rectangle collide, adds 1 to score and removes ball from array and screen
        for ball in self.balls:
            if ball.rect.colliderect(self.player.rect):
                if type(ball) is PowerBall:
                    ball.power_up(self.player)
                self.balls.pop(self.balls.index(ball))
                self.score += 1

    def showtext(self):
        text = self.smallfont.render("Caught: " + str(self.score), True, (255, 255, 255))
        if self.ball_counter == 50 and not self.balls:
            text = self.smallfont.render("Game over! You caught: " + str(self.score) + " out of: " + str(self.ball_counter), True, (255, 255, 255))
        textrect = self.screen.get_rect().topleft
        self.screen.blit(text, textrect)

if __name__ == '__main__':
    if _test:
            print("In __main__")
    cb = CatchBall()
    cb.run_game()