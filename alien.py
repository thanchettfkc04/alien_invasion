import pygame, sys
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        '''Set chỉ số cho Alien'''
        super(Alien, self).__init__()
        self.screen =screen
        self.ai_settings = ai_settings

        #load ảnh và set chỉ số
        self.image = pygame.image.load('img/enemy.png')
        self.rect = self.image.get_rect()

        #set alien ở đầu screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #giữ tọa độ x để chỉnh sửa
        self.x = float(self.rect.x)

    def blitme(self):
        """Ve alien tai current possition"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        # Trả về giá trị True nếu nó reach cạnh màn hình, trái thì âm, phải thì max
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True