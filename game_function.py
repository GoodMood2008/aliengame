#!/usr/bin/python
#-*- coding:utf-8 -*-
import pygame
import sys
from bullet import Bullet
from ship import Ship
from settings import Settings
from alient import Alien
from time import sleep


def update_screen(ai_settings, screen, ship, aliens, bullets, sb, stats, play_button):

    # 每次循环绘制屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()

    #dispay score
    sb.show_score()

    # if game is not acitve, draw button
    # draw button at last to keep button is upper all the other image
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()





def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    return int(available_space_y / (2 * alien_height))


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alient_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alient_width
    number_alient_x = int(available_space_x/(2*alient_width))
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alient_number in range(number_alient_x):
            create_alien(ai_settings, aliens, alient_number, alient_width, screen, row_number)


def create_alien(ai_settings, aliens, alient_number, alient_width, screen, row_number):
    alien = Alien(ai_settings, screen)
    alien.x = alient_width + 2 * alient_number * alient_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * row_number * alien.rect.height
    aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #if collide with ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    #clear aliens and bullet
    aliens.empty()
    bullets.empty()

    #create new alien and ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    #sleep
    sleep(0.5)


def check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button):
    # supervisor keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_down_event_up(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y):
    # player click play to begin game
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if not stats.game_active and button_click:
        #reset game settings
        ai_settings.initial_dynamic_settings()

        #hide the mouse
        pygame.mouse.set_visible(False)

        #emtpy stat
        stats.reset_stats()
        stats.game_active = True

        #empty alien and bullet
        aliens.empty()
        bullets.empty()

        #create alien and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_down_event_up(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_key_down_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    #elif event.key == pygame.K_SPACE:
    elif event.key == pygame.K_m:
        fire_bullet(ai_settings, bullets, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, bullets, screen, ship):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, ship, aliens, bullets, sb, stats):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship, sb, stats)


def check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship, sb, stats):
    # check bullet shot alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score
    if len(aliens) == 0:
        # delete all bullet, accelareate speed, and careate a new aliens
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)