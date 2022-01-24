import pygame

class Player:
    def __init__(self, cb_game):
        self.screen = cb_game.screen
        self.screen_rect = cb_game.screen.get_rect()
        self.img = pygame.image.load("imgs/dog.png")
        self.img = pygame.transform.scale(self.img, (50, 50))
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
            if self.rect.x + self.vel <= 450:
                self.rect.x += (self.vel + 1)
            else:
                self.rect.x = 445
        if self.left:
            if self.rect.x -self.vel >= -20:
                self.rect.x -= self.vel
            else:
                self.rect.x = -15
        if self.up:
            if self.rect.y -self.vel >= -20:
                self.rect.y -= self.vel
            else:
                self.rect.y = -15
        if self.down:
            if self.rect.y + self.vel <= 450:
                self.rect.y += (self.vel + 1)
            else:
                self.rect.y = 445
                
    #Updates screen with new player position
    def blit_player(self):
        self.screen.blit(self.img, self.rect)
        