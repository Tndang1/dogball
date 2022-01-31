import random
from ball import Ball
import pygame
from player import Player

class PowerBall(Ball):
    def __init__(self, cb_game):
        super().__init__(cb_game)

    def power_up(self, player):
        print ('************' + str(player.vel))
        chance = random.randint(1,2)
        if chance == 1:
            self.speed_up(player)
        if chance == 2:
            self.size_up(player)

    def speed_up(self, player):
        if player.vel < 2:
            player.vel += 0.5
        else:
            player.vel += 0.1
    
    def size_up(self, player):
        x = player.rect.x
        y = player.rect.y
        player.img = pygame.transform.scale(player.img, (70, 70))
        player.rect = player.img.get_rect()
        player.rect.x = x
        player.rect.y = y