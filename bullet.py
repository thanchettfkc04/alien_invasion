import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # Class này sẽ quản lý việc viên đạn bắn ra như thế nào
    def __init__(self, ai_settings, screen, ship):
        # Tạo viên đạn object tại vị trí của tàu
        super(Bullet, self).__init__()
        self.screen = screen

        # Tạo khối cho bullet tại tọa độ 0-0 và set lại vị trí cho nó
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx       # Gán tọa độ trung tâm của đạn bằng trung tâm tàu
        self.rect.top = ship.rect.top               # Gán tọa độ trên cùng của đạn bằng trên cùng của tàu

        # Lưu lại vị trí của đạn dưới dạng thập phân ở 1 biến khác
        # để sau có thể tinh chỉnh tốc độ bằng phép toán
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Mục đích : Tạo chuyển động hướng lên cho viên đạn"""
        #Cập nhật vị trí viên đạn theo chiều y cho cảm giác di chuyển
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)