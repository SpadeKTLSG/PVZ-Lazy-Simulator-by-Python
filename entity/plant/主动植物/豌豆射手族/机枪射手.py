# -*- coding: utf-8 -*-
import pygame

from 主动植物.主动植物基类 import 主动植物基类
from 投掷物.豌豆 import Pea


class 机枪射手(主动植物基类):
    picture = 'resource/image/plant/机枪射手/机枪射手.png' 
    card_picture = 'resource/image/plant/机枪射手/卡片.png' 
    name = '机枪射手'
    sunCost = 400 
    
    attack_speed = 2

    def __init__(self, x, y):
        super().__init__(x, y)
        
    def attack(self): 
        pygame.mixer.Sound('resource/audio/plant/豌豆射手/豌豆发射.ogg').play()
        # future update: match multiple return spirit
        return [Pea(self.x, self.y),Pea(self.x+2, self.y),Pea(self.x+4, self.y),Pea(self.x+6, self.y)]
        
