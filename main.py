
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Ailen Invasion')

    #Tao button
    play_button = Button(ai_settings, screen, "Play")
    #Tao instance de luu lai game stat
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Tạo object ship
    ship = Ship(ai_settings, screen)
    # Tạo 1 group để chứa các bullet
    bullets = Group()
    # Tạo 1 con alien
    # alien = Alien(ai_settings, screen)
    aliens = Group()
    #Tạo fleet của alien
    gf.create_fleet(ai_settings, screen, ship, aliens)



    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)


        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        pygame.display.flip()

run_game()
