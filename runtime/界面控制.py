# -*- coding: utf-8 -*-
import sys

import pygame

from 全局配置 import 屏幕宽度, 屏幕高度
from 实体列表 import plant_list

# 正式版本
version = "1.5.2 人事已尽"

def 初始化界面(screen):

    bg = pygame.image.load("resource/image/system/通用/背景.jpg").convert()
    screen.blit(bg, (0, 0))
    bg1 = pygame.image.load("resource/image/system/通用/地图.jpg").convert()
    screen.blit(bg1, (0, 100))
    tool_bar = pygame.image.load("resource/image/system/控制栏/上方面板.png").convert_alpha()
    screen.blit(tool_bar, (0, 0))
    shovel = pygame.image.load("resource/image/system/控制栏/铲子.png").convert_alpha()
    screen.blit(shovel, (400, 20))
    menu_button = pygame.image.load("resource/image/system/菜单/暂停菜单.png").convert_alpha()
    screen.blit(menu_button, (650, 0))
    new_card_list = [p for up in plant_list for p in up]
    for o in new_card_list:
        plantcard = pygame.image.load("resource/image/plant/" + o + "/卡片.png").convert_alpha()
        plantcard = pygame.transform.scale(plantcard, (round(750 * 0.07), round(600 * 0.12)))
        screen.blit(plantcard, (90 + new_card_list.index(o) * 85, 10))
    pygame.display.flip()


def 引导界面(screen):
    pygame.init()
    pygame.display.set_caption('PVZ')
    
    clock = pygame.time.Clock()
    clock.tick(24) # 帧率?
    
    font1 = pygame.font.Font('resource/font/SimHei.ttf', 20)
    fontx = pygame.font.Font('resource/font/SimHei.ttf', 60)

    bg4 = pygame.image.load("resource/image/system/菜单/开始界面.jpg").convert_alpha()  # 重设大小
    bg4 = pygame.transform.scale(bg4, (1440, 700))  # 全屏覆盖    
    screen.blit(bg4, (0, 0))
    bg4 = pygame.image.load("resource/image/system/菜单/Logo.jpg").convert_alpha()  # 重设大小
    bg4 = pygame.transform.scale(bg4, (750, 120))
    screen.blit(bg4, (0, 0))
    bg4 = pygame.image.load("resource/image/system/菜单/草3.png").convert_alpha()  # 重设大小
    screen.blit(bg4, (200, 400))
    bg4 = pygame.image.load("resource/image/system/菜单/草1.png").convert_alpha()  # 重设大小
    screen.blit(bg4, (200, 500))
    bg4 = pygame.image.load("resource/image/system/菜单/草2.png").convert_alpha()  # 重设大小
    screen.blit(bg4, (505, 560))

    text2 = font1.render("V. " + version, True, (0, 0, 240))
    screen.blit(text2, (540, 570))
    text2 = font1.render("by SpadeKXRM", True, (0, 0, 240))
    screen.blit(text2, (15, 570))
    text2 = fontx.render("按任意键显示攻略", True, (0, 0, 240))
    screen.blit(text2, (140, 170))

    # 1.进入商店
    bx1, by1, bw1, bh1 = 250, 500, 200, 50  
    pygame.draw.rect(screen, (255, 0, 0), (bx1, by1, bw1, bh1))
    text1 = font1.render("我要氪金", True, (114, 114, 114))
    tw1, th1 = text1.get_size()
    tx1, ty1 = bx1 + bw1 / 2 - tw1 / 2, by1 + bh1 / 2 - th1 / 2
    screen.blit(text1, (tx1, ty1))

    # 2.进入游戏
    bx2, by2, bw2, bh2 = 250, 420, 200, 50
    pygame.draw.rect(screen, (0, 255, 0), (bx2, by2, bw2, bh2))
    text2 = font1.render("直接来吧", True, (114, 51, 4))
    tw2, th2 = text2.get_size()
    tx2, ty2 = bx2 + bw2 / 2 - tw2 / 2, by2 + bh2 / 2 - th2 / 2
    screen.blit(text2, (tx2, ty2))
    pygame.display.flip()

    while True:

        for beevent in pygame.event.get():
            if beevent.type == pygame.QUIT:
                pygame.mixer.Sound("resource/audio/shop/IamWrong.ogg").play()
                pygame.time.delay(2000) # 吼叫退出
                pygame.quit()
                sys.exit()

            if beevent.type == pygame.MOUSEBUTTONDOWN:
                nmx, nmy = beevent.pos
                if bx1 + bw1 >= nmx >= bx1 and by1 + bh1 >= nmy >= by1:
                    pygame.draw.rect(screen, (200, 200, 200), (bx1, by1, bw1, bh1)) 
                    screen.blit(text1, (tx1, ty1))
                    pygame.display.update()
                elif bx2 + bw2 >= nmx >= bx2 and by2 + bh2 >= nmy >= by2:
                    pygame.draw.rect(screen, (200, 200, 200), (bx2, by2, bw2, bh2))
                    screen.blit(text2, (tx2, ty2))
                    pygame.display.update()

            if beevent.type == pygame.MOUSEBUTTONUP:
                nmx, nmy = beevent.pos 
                if bx1 + bw1 >= nmx >= bx1 and by1 + bh1 >= nmy >= by1:
                    pygame.draw.rect(screen, (255, 0, 0), (bx1, by1, bw1, bh1))
                    screen.blit(text1, (tx1, ty1))
                    pygame.display.update()
                    # 进入商店
                    商店界面(screen)
                    return

                elif bx2 + bw2 >= nmx >= bx2 and by2 + bh2 >= nmy >= by2:
                    pygame.draw.rect(screen, (0, 255, 0), (bx2, by2, bw2, bh2))
                    screen.blit(text2, (tx2, ty2))
                    pygame.display.update()
                    # 进入商店
                    return
            if beevent.type==pygame.KEYDOWN: #显示攻略
                bg4 = pygame.image.load("resource/image/system/通用/笔记.png").convert_alpha()  # 重设大小
                bg4=pygame.transform.scale(bg4,(屏幕宽度,屏幕高度))
                screen.blit(bg4, (0, 0))
                pygame.display.update()
                # 播放戴夫的吼叫
                pygame.mixer.Sound("resource/audio/shop/进场戴夫 (1).ogg").play()
                pygame.time.delay(3000) #暂停3秒
                return


def 商店界面(screen):
    font2 = pygame.font.Font('resource/font/Inkfree.ttf', 20)
    font3 = pygame.font.Font('resource/font/Inkfree.ttf', 80)

    bg4 = pygame.image.load("resource/image/system/商店/超商背景.jpg").convert_alpha()
    screen.blit(bg4, (0, 0))
    bg4 = pygame.image.load("resource/image/system/商店/戴夫肉.png").convert_alpha()
    screen.blit(bg4, (300, 400))
    bg4 = pygame.image.load("resource/image/system/商店/高坚果.png").convert_alpha()
    bg4 = pygame.transform.smoothscale(bg4, (300, 350))
    screen.blit(bg4, (300, 110))
    bg4 = pygame.image.load("resource/image/system/商店/猫耳.png").convert_alpha()
    bg4 = pygame.transform.smoothscale(bg4, (250, 300))
    screen.blit(bg4, (300, 20))
    bg4 = pygame.image.load("resource/image/system/商店/火.png").convert_alpha()
    bg4 = pygame.transform.smoothscale(bg4, (450, 280))
    screen.blit(bg4, (250, 370))
    bg4 = pygame.image.load("resource/image/system/商店/超市货物.png").convert_alpha()
    bg4 = pygame.transform.smoothscale(bg4, (200, 200))
    screen.blit(bg4, (180, 390))
    bg4 = pygame.image.load("resource/image/system/商店/超市货物.png").convert_alpha()
    bg4 = pygame.transform.smoothscale(bg4, (200, 200))
    screen.blit(bg4, (480, 290))
    bg4 = pygame.image.load("resource/image/system/控制栏/阳光.png").convert_alpha()
    bg4 = pygame.transform.smoothscale(bg4, (200, 200))
    screen.blit(bg4, (520, 30))
    text1 = font3.render("Shop", True, (0, 0, 114))
    screen.blit(text1, (60, 200))

    # 进入游戏按钮
    bx1, by1, bw1, bh1 = 250, 500, 200, 50
    pygame.draw.rect(screen, (255, 0, 0), (bx1, by1, bw1, bh1))
    text1 = font2.render("Let's Rock", True, (0, 0, 114))
    tw1, th1 = text1.get_size()
    tx1, ty1 = bx1 + bw1 / 2 - tw1 / 2, by1 + bh1 / 2 - th1 / 2
    screen.blit(text1, (tx1, ty1))
    pygame.display.flip()

    # 2.充值按钮
    bx2, by2, bw2, bh2 = 250, 420, 200, 50
    pygame.draw.rect(screen, (0, 255, 0), (bx2, by2, bw2, bh2))
    text2 = font2.render("moneymoneymoney", True, (0, 5, 14))
    tw2, th2 = text2.get_size()
    tx2, ty2 = bx2 + bw2 / 2 - tw2 / 2, by2 + bh2 / 2 - th2 / 2
    screen.blit(text2, (tx2, ty2))
    pygame.display.flip()
    pygame.mixer.Sound("resource/audio/shop/进场戴夫 (2).ogg").play()


    while True:

        for kevent in pygame.event.get():
            if kevent.type == pygame.QUIT:
                pygame.mixer.Sound("resource/audio/shop/IamWrong.ogg").play()
                pygame.time.delay(2000) # 吼叫退出
                pygame.quit()
                sys.exit()

            if kevent.type == pygame.MOUSEBUTTONDOWN:
                nmx, nmy = kevent.pos 
                if bx1 + bw1 >= nmx >= bx1 and by1 + bh1 >= nmy >= by1:
                    pygame.draw.rect(screen, (200, 200, 200), (bx1, by1, bw1, bh1))  
                    screen.blit(text1, (tx1, ty1))
                    pygame.display.update()
                elif bx2 + bw2 >= nmx >= bx2 and by2 + bh2 >= nmy >= by2:
                    pygame.draw.rect(screen, (200, 200, 200), (bx2, by2, bw2, bh2))
                    screen.blit(text2, (tx2, ty2))
                    pygame.display.update()

            if kevent.type == pygame.MOUSEBUTTONUP:
                nmx, nmy = kevent.pos  
                if bx1 + bw1 >= nmx >= bx1 and by1 + bh1 >= nmy >= by1:
                    pygame.draw.rect(screen, (255, 0, 0), (bx1, by1, bw1, bh1))
                    screen.blit(text1, (tx1, ty1))
                    pygame.display.update()
                    return

                elif bx2 + bw2 >= nmx >= bx2 and by2 + bh2 >= nmy >= by2:
                    pygame.draw.rect(screen, (0, 255, 0), (bx2, by2, bw2, bh2))
                    screen.blit(text2, (tx2, ty2))
                    pygame.display.update()
                    pygame.mixer.Sound("resource/audio/shop/进场戴夫 (1).ogg").play()
                    screen.fill((0, 0, 0))
                    meat = pygame.image.load("resource/image/system/商店/收款码.png").convert_alpha()  # 调整大小
                    meat = pygame.transform.scale(meat, (600, 600))
                    screen.blit(meat, (75, 0))
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    pygame.mixer.Sound("resource/audio/shop/进场戴夫 (3).ogg").play()
                    
                    while True:
                        for gevent in pygame.event.get():
                            if gevent.type == pygame.QUIT:
                                pygame.mixer.Sound("resource/audio/shop/IamWrong.ogg").play()
                                pygame.time.delay(2000) 
                                pygame.quit()
                                sys.exit()

                            if gevent.type == pygame.MOUSEBUTTONDOWN:
                                print('氪金不能让你更强.(也不能给你加阳光)')
                                pygame.mixer.Sound("resource/audio/shop/IamWrong.ogg").play()
                                return

def 失败退出(screen):
    bg2 = pygame.image.load("resource/image/system/通用/背景.jpg").convert_alpha()
    screen.blit(bg2, (0, 0))
    bg2 = pygame.image.load("resource/image/system/事件/失败页面.png").convert_alpha()
    bg2 = pygame.transform.scale(bg2, (800, 600))
    screen.blit(bg2, (-25, 0))
    pygame.display.flip()

    pygame.mixer.Sound("resource/audio/event/啃脑子.ogg").play()
    pygame.time.delay(500)
    pygame.mixer.Sound("resource/audio/event/啃脑子2.ogg").play()
    pygame.time.delay(1000)
    pygame.mixer.Sound("resource/audio/event/啃脑子2.ogg").play()
    pygame.time.delay(1000)
    pygame.mixer.Sound("resource/audio/event/啃脑子.ogg").play()
    pygame.mixer.Sound("resource/audio/event/失败音乐.ogg").play()

    while True:
        for event3 in pygame.event.get():
            if event3.type == pygame.QUIT:
                pygame.mixer.Sound("resource/audio/shop/IamWrong.ogg").play()
                pygame.time.delay(2000) 
                pygame.quit()
                sys.exit()
            if event3.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
                
                

def 胜利退出(screen):
    bg = pygame.image.load("resource/image/system/通用/背景.jpg").convert_alpha()
    screen.blit(bg, (0, 0))
    cup = pygame.image.load("resource/image/system/事件/奖杯.png").convert_alpha()
    cup = pygame.transform.scale(cup, (200, 250))
    screen.blit(cup, (275, 200))

    font = pygame.font.Font('resource/font/Inkfree.ttf', 60)
    text = font.render("Enjoy your time! : )", True, (255, 255, 255))
    screen.blit(text, (350, 500))
    font5 = pygame.font.Font('resource/font/Inkfree.ttf', 80)
    text5 = font5.render("By SpadeKXRM", True, (255, 0, 255))
    screen.blit(text5, (0, 0))
    pygame.display.flip()
    pygame.mixer.Sound('resource/audio/else/主题曲.ogg').play()

    while True:
        for event3 in pygame.event.get():
            if event3.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event3.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()