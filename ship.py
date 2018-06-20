#!/usr/bin/python
#-*- coding:utf-8 -*-

import pygame

class Ship(object):
    def __init__(self, ai_settings, screen):
        self.screen = screen

        self.image = pygame.image.load('image/redship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.ai_settings = ai_settings

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.rect.bottom -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.ai_settings.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)