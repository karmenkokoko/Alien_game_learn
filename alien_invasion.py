import sys

import pygame

from Alien_game.ship import Ship
from Alien_game.settings import Settings
from Alien_game.alien import Alien
from Alien_game.game_stats import GameStats
from Alien_game.button import Button
from Alien_game.scoreboard import Scoreboard
import Alien_game.game_functions as gf
from pygame.sprite import Group

def run_game():
    #initial game
    pygame.init()
    #initial settings
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings,screen,"Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #create a ship
    ship=Ship(ai_settings,screen)
    #store bullets group
    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()