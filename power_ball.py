import random
import pygame

from ball import Ball

class PowerBall(Ball):
    def __init__(self, cb_game):
        super().__init__(cb_game)
        self.img = pygame.image.load("imgs/powerball.png")
        self.img = pygame.transform.scale(self.img, (15, 15))

    def power_up(self, player):
        chance = random.randint(1,3)
        if chance < 3:
            self.speed_up(player)
        if chance == 3:
            self.size_up(player)

    def speed_up(self, player):
        if player.vel < 3:
            player.vel += 0.5
        else:
            player.vel += 0.2

    def size_up(self, player):
        #save current position of player
        x = player.rect.x
        y = player.rect.y
        #transform player size
        player.player_width += random.randint(7,20)
        player.player_height += random.randint(7,20)
        player.img = pygame.transform.scale(player.img, (player.player_width, player.player_height))
        player.rect = player.img.get_rect()
        #set player in original location
        player.rect.x = x
        player.rect.y = y