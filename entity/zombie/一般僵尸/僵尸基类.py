# -*- coding: utf-8 -*-
from random import randint

import pygame
from pygame.sprite import Sprite

from 全局配置 import Sizes


class 僵尸基类(Sprite):
    寻路装置 = [2, 1, 2, 1, 2, 1, 2, 1, 4, 1, 4, 1, 4, 1, 1, 1, 1] #后面的1防止溢出
    寻路指针 = 0  # 寻路装置中的位置
    单元格位置 = 0  # 单元格中的位置,达到4就读取寻路装置的下一个方向

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = None  # type: pygame.Surface  # 僵尸图片
        self.picture = None  # type: str # 僵尸图片路径
        self.card_picture = None  # 僵尸卡片图片
        self.name = 'cwx'  # 僵尸的名字
        self.sound = []  # type: [pygame.mixer.Sound] # 僵尸音效,固定刚好3个, 分别是叫声, 死亡声, 被臭晕声
        self.rect = None  # type: pygame.Rect # 僵尸矩形

        # 各自的属性
        self.speed = 0
        self.hp = 100

    def get_picture(self):
        return self.picture

    def get_image(self):  # 获取僵尸转换完成的图片
        return self.image

    def get_card_picture(self):  # 获取僵尸卡片图片
        return self.card_picture

    def talk(self):  # 僵尸的10s自动更新叫声
        pygame.mixer.Sound(self.sound[0]).play()

    def rip(self):  # 僵尸死亡音效
        pygame.mixer.Sound(self.sound[1]).play()

    def shit(self):  # 僵尸被臭晕的叫声
        pygame.mixer.Sound(self.sound[2]).play()

    def draw(self, screen):  # 调用方法画出来
        screen.blit(self.image, (self.x, self.y))

    def update(self, screen):  # 刷新时有概率说话, 概率为15%
        tick = randint(0, 100)
        if tick > 85:
            pygame.mixer.Sound(self.sound[0]).play()
            
        if self.hp <= 0:  # 血量小于等于0, 就死亡
            self.rip()
            self.kill()
            return 0

        if self.x <= -100:  # 手动判定到达家门口
            return 1

        self.get_position(screen)
        self.draw(screen)

    def get_position(self, screen):  # 辅助更新
        if self.单元格位置 <= 3:
            # 在单元格内移动:
            toward = self.寻路装置[self.寻路指针]  # 获得当前移动的方向
            # 基础单位移动的计算: 确认是单元格内的移动后: 横坐标-四分之一的网格宽度乘上速度量

            if toward == 1:  # 向左移动
                self.x -= self.speed * 0.25 * Sizes["grid"][0]
            if toward == 2:  # 向下移动
                self.y += self.speed * 0.25 * Sizes["grid"][1]
            if toward == 3:  # 向右移动
                self.x += self.speed * 0.25 * Sizes["grid"][0]
            if toward == 4:  # 向上移动
                self.y -= self.speed * 0.25 * Sizes["grid"][1]

            self.draw(screen)  # type: pygame.Surface
            self.单元格位置 += self.speed  # 单元格位置+self.speed
        else:
            pygame.mixer.Sound(self.sound[2]).play()  # 发生了切换单元格的情况:被臭晕的音乐播放
            self.单元格位置 = 0  # 重置单元格位置
            self.寻路指针 += 1  # 寻路指针+1
            toward = self.寻路装置[self.寻路指针]  # 获得新的寻路指针对应的方向

            if toward == 1:  # 向左移动到下一个单元格
                self.x -= self.speed * 0.25 * Sizes["grid"][0]
            if toward == 2:  # 向下移动到下一个单元格
                self.y += self.speed * 0.25 * Sizes["grid"][1]
            if toward == 3:  # 向右移动到下一个单元格
                self.x += self.speed * 0.25 * Sizes["grid"][0]
            if toward == 4:  # 向上移动到下一个单元格
                self.y -= self.speed * 0.25 * Sizes["grid"][1]
