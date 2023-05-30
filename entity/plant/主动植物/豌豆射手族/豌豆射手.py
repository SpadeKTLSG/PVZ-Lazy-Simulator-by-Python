# -*- coding: utf-8 -*-
import pygame

from 主动植物.主动植物基类 import 主动植物基类
from 投掷物.豌豆 import Pea


class 豌豆射手(主动植物基类):
    picture = 'resource/image/plant/豌豆射手/豌豆射手.png' 
    card_picture = 'resource/image/plant/豌豆射手/卡片.png' 
    name = '豌豆射手'
    sunCost = 100 
    
    attack_speed = 2
    # 攻击方式: 发射豌豆,造成普通僵尸1/10血量的伤害(10)

    def __init__(self, x, y):
        super().__init__(x, y)
        
    def attack(self): 
        pygame.mixer.Sound('resource/audio/plant/豌豆射手/豌豆发射.ogg').play()
        return Pea(self.x, self.y)
