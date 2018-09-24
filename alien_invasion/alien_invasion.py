# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 23:06:02 2018
@author: Summerhack
"""
import pygame

from pygame.sprite import Group
from alien import Alien
import game_functions as gf

from ship import Ship
from settings import Settings

def run_game():
    #初始化一个游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.scree_width, ai_settings.scree_height))    #设置屏幕像素值
    pygame.display.set_caption("Aline Invasion")     #显示游戏名称
    
    #创建一个新飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个新外星人
    alien = Alien(ai_settings, screen)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)    #监视键盘和鼠标事件
        ship.update()            #更新飞船位置
        gf.update_screen(ai_settings, screen, ship, alien, bullets)   #重绘并显示新屏幕
        gf.update_bullets(bullets)


        

run_game()
    
    

