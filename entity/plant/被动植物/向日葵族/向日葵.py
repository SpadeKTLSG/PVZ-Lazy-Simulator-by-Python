# -*- coding: utf-8 -*-
from 被动植物.被动植物基类 import 被动植物基类


class 向日葵(被动植物基类):
    picture = 'resource/image/plant/向日葵/向日葵.png'  # 植物的图片
    card_picture = 'resource/image/plant/向日葵/飞贼僵尸.png'  # 植物的卡片图片
    name = '向日葵'  # 植物的名字
    # 被动植物特性
    sunCost = 50  # 植物的阳光消耗

    # 产生阳光计数: 普通的向日葵等于1个阳光产能, 双倍向日葵等于2个阳光产能
    sunpowerCount = 1

    def __init__(self, x, y):
        super().__init__(x, y)

    # 获取信息方法, 真正调用的时候, 会调用植物基类的方法然后强制转换为被动植物族的方法
    # 同时会封装全部调用为一次, 以便于调用者调用
    # 以下是特有方法

    def get_sunpowerCount(self):  # 获取植物阳光产能
        return self.sunpowerCount
