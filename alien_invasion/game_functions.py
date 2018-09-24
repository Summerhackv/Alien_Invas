# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 22:23:19 2018

@author: Summerhack
"""

import sys
import pygame

from bullet import Bullet

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


def update_screen(ai_settings, screen, ship, alien, bullets):
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
        
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

    