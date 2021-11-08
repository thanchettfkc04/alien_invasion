import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Setting vị trí khởi đầu của ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        # Cờ hiệu để đánh dấu movemented
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Update vị trí của tàu, không phải vị trí của khối rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #Update lại vị trí khối rect theo vị trí tàu
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
