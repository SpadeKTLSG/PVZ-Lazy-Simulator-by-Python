# -*- coding: utf-8 -*-
import pygame

from 全局配置 import 屏幕宽度, Sizes
from 投掷物基类 import Projectile


class Corn(Projectile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        # 各自的属性
        self.speed = 50  # 速度为500像素点每次移动,超级快,这样也是一种追踪(不是摸鱼)
        self.damage = 1000  # 正常伤害为1000(巨人的一半)

        self.sound = "resource/audio/plant/玉米加农炮/玉米命中.ogg"
        temp_image = pygame.image.load("resource/image/plant/玉米加农炮/玉米子弹.png").convert_alpha()
        self.image = pygame.transform.scale(temp_image, Sizes["giant_projectile"])
        self.rect = self.image.get_rect()
        self.is_hit = False  # 是否击中, 用于判断是否播放爆炸效果

    def update(self, screen):
        self.x += self.speed
        self.draw(screen)  # type: pygame.Surface
        if self.x >= 屏幕宽度 or self.is_hit:# 伤害后并且更新了一次后自杀
            self.kill()


    def hit(self, target):
        target.hp -= self.damage
        pygame.mixer.Sound(self.sound).play() # 加农炮效果: 替换贴图进行一次更新
        temp_image = pygame.image.load("resource/image/plant/玉米加农炮/炮弹爆炸.png").convert_alpha()
        self.image = pygame.transform.scale(temp_image, Sizes["effect"])
        self.is_hit = True  # 击中标记
