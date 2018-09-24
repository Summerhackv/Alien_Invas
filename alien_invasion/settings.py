# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 21:37:45 2018
@author: Summerhack
"""
 #存储《外星人入侵》的所有设置参数
class Settings():
   
    #初始化游戏设置
    def __init__(self):
        
        #屏幕设置
        self.scree_width = 1200
        self.scree_height = 800
        self.bg_color = (230, 230, 230)
        
        #飞船速度设置
        self.ship_speed_factor = 1.5
        
        #子弹设置
        self.bullet_speed_factor = 1    #子弹速度
        self.bullet_width = 3           #子弹宽度
        self.bullet_heigh = 15          #子弹长度
        self.bullet_color = 60, 60, 60  #子弹颜色
        self.bullets_allowed = 3         #未消失的子弹数目


        
        
        
