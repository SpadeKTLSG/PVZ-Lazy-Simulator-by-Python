# -*- coding: utf-8 -*-
import pygame

from 主动植物.玉米加农炮族.玉米加农炮 import 玉米加农炮
from 植物基类 import 植物基类
from 主动植物.西瓜投手族.西瓜投手 import 西瓜投手
from 主动植物.豌豆射手族.豌豆射手 import 豌豆射手
from 被动植物.向日葵族.向日葵 import 向日葵


def summon_plant(name, x, y):  # 直接传入植物的名字, 返回植物的图片
    plant = 植物基类(x, y)
    if name == '向日葵':
        plant = 向日葵(x,y)

    elif name == '豌豆射手':
        plant = 豌豆射手(x, y)

    elif name == '西瓜投手':
        plant = 西瓜投手(x,y)

    elif name =='玉米加农炮':
        plant = 玉米加农炮(x,y)
        
    plant = pygame.image.load(plant.get_picture()).convert_alpha()
    plant = pygame.transform.scale(plant, (round(750 * 0.1), round(600 * 0.2)))

    return plant


def summon_plant_class(name, x, y):  # 直接传入植物的名字, 返回植物的类
    plant = 植物基类(x, y)
    if name == '向日葵':
        plant = 向日葵(x,y)

    elif name == '豌豆射手':
        plant = 豌豆射手(x, y)

    elif name == '西瓜投手':
        plant = 西瓜投手(x,y)
        
    elif name =='玉米加农炮':
        plant = 玉米加农炮(x,y)

    return plant
