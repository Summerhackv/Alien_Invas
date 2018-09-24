# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 22:23:19 2018

@author: Summerhack
"""

import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:     #检测键盘向右
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:    #检测键盘向左
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
              
def check_keyup_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:           #检测到关闭信号，就退出pygame，关闭程序
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:      #检测键盘向右
                check_keydown_events(event, ai_settings, screen, ship, bullets)
                    
            elif event.type == pygame.KEYUP:    
                check_keyup_events(event, ship)
                
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #alien.blitme()
        
    #显示最近绘制屏幕
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def creat_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #创建一个外星人并将其加入当前行
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_alien_x(ai_settings, alien_width):
    """计算每行可以容纳多少外星人"""
    available_space_x = ai_settings.scree_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 *alien_width))
    return number_aliens_x

def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少外星人"""
    available_space_y = (ai_settings.scree_height -
                         (3 * alien_height) - ship_height)
    number_rows = int (available_space_y / (2 * alien_height))
    return number_rows

