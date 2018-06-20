#!/usr/bin/python
#-*- coding:utf-8 -*-

class Settings(object):
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 750
        self.bg_color = (0xE0, 0xFF, 0xFF)
        self.ship_limit = 3

        #bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10

        #alien
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #accelerate game speed
        self.speedup_scale = 1.1
        self.initial_dynamic_settings()


    def initial_dynamic_settings(self):
        #init speed factors
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        # alient directory
        self.fleet_direction = 1

        # socre
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale