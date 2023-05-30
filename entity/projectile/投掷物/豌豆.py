# -*- coding: utf-8 -*-
import pygame

from 全局配置 import 屏幕宽度, Sizes
from 投掷物基类 import Projectile


class Pea(Projectile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.speed = 240
        self.damage = 10
        
        self.sound = "resource/audio/plant/豌豆射手/豌豆命中.ogg"
        temp_image = pygame.image.load("resource/image/plant/豌豆射手/豌豆子弹.png").convert_alpha() 
        self.image = pygame.transform.scale(temp_image, Sizes["projectile"])
        self.rect = self.image.get_rect()  # type: pygame.Rect

    def update(self, screen):
        self.x += self.speed
        self.draw(screen)  # type: pygame.Surface
        if self.x >= 屏幕宽度:
            self.kill()
 
    