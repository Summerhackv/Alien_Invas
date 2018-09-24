import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置初始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置rect属性
        self.imag = pygame.image.load('images/alien.bmp')
        self.rect = self.imag.get_rect()

        # 每个外星人最初都在屏幕左上方移动
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储每个外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.imag, self.rect)


