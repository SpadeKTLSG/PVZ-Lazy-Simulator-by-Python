# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Projectile(Sprite):

    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y
        self.image = None  # type: pygame.Surface #投掷物图片
        self.sound = None  # type: str #投掷物音效str
        self.rect = None  # type: pygame.Rect #投掷物矩形

        # 各自的属性
        self.speed = 0
        self.damage = 0

    def hit(self, target):
        target.hp -= self.damage
        pygame.mixer.Sound(self.sound).play()
        self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, screen): 
        pass
