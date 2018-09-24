# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:18:06 2018

@author: Summerhack
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对飞船发射进行管理的类"""
    
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_heigh)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #存储用小数表示子弹的位置
        self.y = float(self.rect.y)
        #存储子弹的颜色
        self.color = ai_settings.bullet_color
        #存储子弹的速度
        self.speed_facotr = ai_settings.bullet_speed_factor
        
    def update(self):
        #更新表示子弹位置的小数值
        self.y -= self.speed_facotr
        #更新表示子弹位置的rect位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        
        
        