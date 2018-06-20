#!/usr/bin/python
#-*- coding:utf-8 -*-

class GameStats():
    def __init__(self, ai_settings):
        #game is active when begin
        self.game_active = False
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0