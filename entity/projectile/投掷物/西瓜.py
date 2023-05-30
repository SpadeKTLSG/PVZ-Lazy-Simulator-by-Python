# -*- coding: utf-8 -*-
import pygame

from 全局配置 import 屏幕宽度, Sizes
from 投掷物基类 import Projectile


class Melon(Projectile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.speed = 220 
        self.damage = 50

        self.sound = "resource/audio/plant/西瓜投手/西瓜命中.ogg"
        temp_image = pygame.image.load("resource/image/plant/西瓜投手/西瓜子弹.png").convert_alpha()
        self.image = pygame.transform.scale(temp_image, Sizes["giant_projectile"])
        self.rect = self.image.get_rect()

    def update(self, screen):
        self.x += self.speed
        self.draw(screen)
        if self.x >= 屏幕宽度:
            self.kill()

        