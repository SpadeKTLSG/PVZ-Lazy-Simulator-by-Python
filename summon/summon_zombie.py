# -*- coding: utf-8 -*-
import pygame

from 一般僵尸.普通僵尸 import 普通僵尸
from 一般僵尸.僵尸基类 import 僵尸基类
from 一般僵尸.自爆僵尸 import 自爆僵尸
from 一般僵尸.路障僵尸 import 路障僵尸


def summon_zombie(name, x, y):  # 直接传入僵尸的名字, 返回僵尸的图片
    zombie = 僵尸基类(x, y)
    if name == '普通僵尸':
        zombie = 普通僵尸(x, y)
    if name == '路障僵尸':
        zombie = 路障僵尸(x, y)
    if name == '自爆僵尸':
        zombie = 自爆僵尸(x, y)

    zombie = pygame.image.load(zombie.get_picture()).convert_alpha()
    zombie = pygame.transform.scale(zombie, (round(750 * 0.1), round(600 * 0.2)))

    return zombie


def summon_zombie_class(name, x, y):  # 直接传入僵尸的名字, 返回僵尸的类
    zombie = 僵尸基类(x, y)
    if name == '普通僵尸':
        zombie = 普通僵尸(x, y) 
    if name == '路障僵尸':
        zombie = 路障僵尸(x, y)
    if name == '自爆僵尸':
        zombie = 自爆僵尸(x, y)
    return zombie
