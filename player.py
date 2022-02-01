import pygame

class Player:
    def __init__(self, cb_game):
        self.screen = cb_game.screen
        self.screen_width = cb_game.screen_width
        self.screen_height = cb_game.screen_height
        self.screen_rect = cb_game.screen.get_rect()
        self.img = pygame.image.load("imgs/dog.png")
        self.player_width = 50
        self.player_height = 50
        self.img = pygame.transform.scale(self.img, (self.player_width, self.player_height))
        self.rect = self.img.get_rect()
        #Set starting position in center of screen
        self.rect.center = self.screen_rect.center
        self.vel = 1.2
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def moving(self):
        # Added + 1 to positive x and y to balance speed vs negative movement
        if self.right:
            if self.rect.x + self.vel <= self.screen_width-self.player_width/2:
                self.rect.x += (self.vel + 1)
            else:
                self.rect.x = self.screen_width-self.player_width/2-5
        if self.left:
            if self.rect.x -self.vel >= -self.player_width/2:
                self.rect.x -= self.vel
            else:
                self.rect.x = -self.player_width/2+5
        if self.up:
            if self.rect.y -self.vel >= -self.player_width/2:
                self.rect.y -= self.vel
            else:
                self.rect.y = -self.player_height/2+5
        if self.down:
            if self.rect.y + self.vel <= self.screen_height-self.player_height/2:
                self.rect.y += (self.vel + 1)
            else:
                self.rect.y = self.screen_height-self.player_height/2-5
                
    #Updates screen with new player position
    def blit_player(self):
        self.screen.blit(self.img, self.rect)
        