# -*- coding: utf-8 -*-
import pygame

from 主动植物.主动植物基类 import 主动植物基类
from 投掷物.西瓜 import Melon


class 西瓜投手(主动植物基类):
    picture = 'resource/image/plant/西瓜投手/西瓜投手.png'
    card_picture = 'resource/image/plant/西瓜投手/卡片.png' 
    name = '西瓜投手' 
    sunCost = 300
    # 主动植物特性

    attack_speed = 4  # 西瓜攻速为每4秒攻击一次
    # 攻击方式:横向发射西瓜,造成标准普通僵尸血量一半的伤害(50)

    def __init__(self, x, y):
        super().__init__(x, y)

    def attack(self):
        pygame.mixer.Sound('resource/audio/plant/西瓜投手/西瓜发射.ogg').play()
        return Melon(self.x, self.y)
   