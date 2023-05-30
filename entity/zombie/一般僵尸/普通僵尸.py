# -*- coding: utf-8 -*-
from random import randint

import pygame

from 一般僵尸.僵尸基类 import 僵尸基类
from 全局配置 import Sizes


class 普通僵尸(僵尸基类):
    # 每次直接移动1/4格, 加上一个列表计数器记录移动次数, 每移动4次, 就移动一格

    def __init__(self, x, y):
        super().__init__(x, y)
        # 为了方便, 直接在这里导入图片变量
        self.picture = 'resource/image/zombie/普通僵尸/普通僵尸.png'  # 僵尸的图片

        temp_image = pygame.image.load("resource/image/zombie/普通僵尸/普通僵尸.png").convert_alpha()  # type: pygame.Surface
        self.image = pygame.transform.scale(temp_image, Sizes["zombie"])  # 导入全局变量的僵尸
        self.rect = self.image.get_rect()  # type: pygame.Rect
        self.card_picture = 'resource/image/zombie/普通僵尸/卡片.png'  # 僵尸的卡片图片
        self.name = '普通僵尸'  # 僵尸的名字
        # 音乐列表: 叫声, 死亡声, 被臭晕声
        self.sound = ['resource/audio/zombie/普通僵尸/说话.ogg', 'resource/audio/zombie/普通僵尸/僵尸倒下.ogg', 'resource/audio/zombie/普通僵尸/僵尸恶心.ogg']

        # 僵尸的属性
        self.speed = 1  # 速度为1单位
        hp = 100  # 僵尸的血量

