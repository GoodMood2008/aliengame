#!/usr/bin/python
#-*- coding:utf-8 -*-

import pygame.font

class ScoreBoard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #prepare score
        self.prep_score()

    def prep_score(self):
        #render socre
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings)

        #put socre ont the right up of the screen
        self.score_rect = self.score_image.get_rect()
        self.screen_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #dispaly score
        self.screen.blit(self.score_image, self.score_rect)