# -*- coding: utf-8 -*-
import pygame

from 主动植物.主动植物基类 import 主动植物基类
from 投掷物.玉米 import Corn


class 玉米加农炮(主动植物基类):
    picture = 'resource/image/plant/玉米加农炮/玉米加农炮.png'
    card_picture = 'resource/image/plant/玉米加农炮/卡片.png'
    name = '玉米加农炮' 
    sunCost = 600
    # 主动植物特性  
    
    attack_speed = 12     # 玉米攻速为每12秒攻击一次
    # 攻击方式:横向发射玉米炮弹,造成标准巨人血量一半的伤害

    def __init__(self, x, y):
        super().__init__(x, y)

    def attack(self):
        pygame.mixer.Sound('resource/audio/plant/玉米加农炮/玉米发射.ogg').play()
        return Corn(self.x, self.y)
      