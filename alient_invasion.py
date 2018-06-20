#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
import pygame



from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alient import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
    # init a screen obj
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #create a ship
    ship = Ship(ai_settings, screen)
    bullets = Group()

    #alien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #stat
    stats = GameStats(ai_settings)

    #button
    play_button = Button(ai_settings, screen, "Play")

    #score
    sb = ScoreBoard(ai_settings, screen, stats)

    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, sb, stats)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, sb, stats, play_button)







run_game()