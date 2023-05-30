# -*- coding: utf-8 -*-
import sys
import pygame
from summon_plant import summon_plant, summon_plant_class
from summon_zombie import summon_zombie_class
from 全局配置 import 屏幕高度, 屏幕宽度
from 条件判断 import 可否在此种植, Change_to_sit
from 游戏状态 import 刷怪表, 初始单元格状态
from 界面控制 import 初始化界面, 引导界面, 失败退出, 胜利退出

# 正式版本 1.5.2 人事已尽

# 控制常量区
当前单元格状态 = 初始单元格状态
清空单元格状态 = 初始单元格状态
胜利 = 0  # 默认失败
主战场 = 1

# 通用screen变量
screen = pygame.display.set_mode((屏幕宽度, 屏幕高度))

# 内置处理界面区
def 胜利界面():
    global 主战场, screen, 胜利
    一键清理()
    一键杀僵()
    note = pygame.image.load("resource/image/system/事件/结束笔记.png").convert_alpha()  # 调整大小
    screen.blit(note, (100, 20))
    pygame.mixer.stop()
    pygame.mixer.Sound("resource/audio/event/胜利音乐.ogg").play()
    pygame.display.flip()
    pygame.time.delay(3000)

    胜利 = 1
    主战场 = 0
    pygame.time.delay(1000)
    while True:
        for sevent in pygame.event.get():
            if sevent.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if sevent.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.flip()
                return


def 失败界面():
    global 主战场, screen
    一键清理()
    一键杀僵()
    主战场 = 0
    return


if __name__ == "__main__":

    引导界面(screen)
    初始化界面(screen)

    # !阳光区
    我的阳光 = 25
    基础阳光产能 = 25


    def 绑定阳光():
        global 我的阳光
        f = pygame.font.Font('resource/font/SimHei.ttf', 30)
        f.set_bold(False)
        text1 = f.render(str(我的阳光), True, (102, 204, 255))
        return text1


    def 被动更新阳光():
        global 我的阳光
        我的阳光 += 基础阳光产能 + len(向日葵List) * 25
        if 我的阳光 > 999:
            我的阳光 = 999  # 阳光上限
        pygame.mixer.Sound("resource/audio/plant/获得阳光.ogg").play()
        pygame.draw.rect(screen, (255, 255, 255), (15, 55, 50, 30), 0)
        screen.blit(绑定阳光(), (20, 55))


    def 阳光够吗(植物):
        global 我的阳光
        temp = 我的阳光 - summon_plant_class(植物, mx, my).sunCost
        if temp < 0:
            pygame.mixer.Sound('resource/audio/event/否定.ogg').play()
            return False
        else:
            我的阳光 = temp
            return True


    # !僵尸区
    当前波数 = 0
    波数指针 = 0

    普通僵尸group = pygame.sprite.Group()
    路障僵尸group = pygame.sprite.Group()
    自爆僵尸group = pygame.sprite.Group()
    僵尸Group = [普通僵尸group, 路障僵尸group, 自爆僵尸group]


    def 生成僵尸():
        global 当前波数, 波数指针
        name = 刷怪表[当前波数][波数指针]  # 从刷怪表中获取当前波数的当前波数指针的僵尸名字
        # print("当前波数:", 当前波数, "当前波数指针:", 波数指针, "当前僵尸名字:", name)
        if name != 0:
            if name == 'EG':  # 僵尸出完了,直接判定胜利
                pygame.mixer.Sound("resource/audio/effect/巨大爆炸.ogg").play()
                胜利界面()

            else:  # print("当前波数:", 当前波数, "当前波数指针:", 波数指针, "当前僵尸名字:", name)
                zombie = summon_zombie_class(name, 680, 50)  # 通过僵尸名字召唤僵尸,需要 if
                普通僵尸group.add(zombie)  # 添加到普通僵尸精灵组

        if 波数指针 < 9:
            波数指针 += 1  # 指针+1
        else:
            pygame.mixer.Sound('resource/audio/zombie/僵尸来了.ogg').play()
            当前波数 += 1
            波数指针 = 0


    def 僵尸一键更新(僵尸group集合):
        global 主战场
        for p in 僵尸group集合:
            for k in p:
                status = k.update(screen)  # 0代表未结束,1代表吃脑子
                if status:
                    pygame.mixer.stop() #暂停背景音乐
                    主战场 = 0


    def 一键杀僵():
        普通僵尸group.empty()


    # !子弹区

    豌豆group, 西瓜group, 玉米group = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    投掷物Group = [豌豆group, 西瓜group, 玉米group]


    def 超级投掷物更新(投掷物group集合, 僵尸group集合):
        for 投掷物group in 投掷物group集合:
            for shot in 投掷物group:
                shot.update(screen)
                for man in 僵尸group集合:
                    for zom in man:
                        if shot.rect.colliderect(zom.rect):
                            shot.hit(zom)


    # !植物区
    豌豆射手List, 西瓜投手List, 玉米加农炮List = [], [], []
    主动植物列表 = [豌豆射手List, 西瓜投手List, 玉米加农炮List]
    向日葵List = []
    被动植物列表 = [向日葵List]


    def 绘制植物(px, py, name):
        Xi, Yi = Change_to_sit(px, py)
        tplant = summon_plant(name, Xi, Yi)
        screen.blit(tplant, (Change_to_sit(mx, my)[0] - tplant.get_width() / 2, Change_to_sit(mx, my)[1] - tplant.get_height() / 2))
        return Xi, Yi


    def 同步攻击计数器(fatherList, songroup):
        for father in fatherList:
            son = father[0].attack()
            songroup.add(son)


    # !事件区
    TimeCycle = pygame.USEREVENT + 1
    玉米攻击周期 = pygame.USEREVENT + 5
    西瓜攻击周期 = pygame.USEREVENT + 4
    豌豆攻击周期 = pygame.USEREVENT + 3
    单位时刻更新 = pygame.USEREVENT + 2
    pygame.time.set_timer(TimeCycle, 5000) #默认模式为快速模式, 5s刷新为一个基础周期
    pygame.time.set_timer(玉米攻击周期, 12000)
    pygame.time.set_timer(西瓜攻击周期, 4000)
    pygame.time.set_timer(豌豆攻击周期, 3000)
    pygame.time.set_timer(单位时刻更新, 1000)


    def 一键清理():
        global 当前单元格状态, 清空单元格状态
        当前单元格状态 = 清空单元格状态
        初始化界面(screen)

    #播放背景音乐(应该能持续到结尾)
    pygame.mixer.Sound('resource/audio/else/Kyle Xian - 植物大战僵尸九周年纪念 BGM串烧.mp3').play()
    
    while 主战场:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  
                kmx, kmy = event.pos 
                if 650 < kmx < 775 and 0 < kmy < 120:
                    pygame.mixer.Sound('resource/audio/else/The World.ogg').play()
                    print("THE WORLD!時よ止まれ!")
                    pygame.time.delay(5000)  # 暂停自己的时间5秒
                    print("時よ動け...")
                    pygame.mixer.Sound('resource/audio/effect/恐怖音效.ogg').play()

            if event.type == pygame.KEYDOWN: 

                if event.key == pygame.K_0:  # 按下0键,召唤铲子隐藏植物
                    一键清理() 

                mx, my = pygame.mouse.get_pos()
                can_plant = 可否在此种植(mx, my, 当前单元格状态)
                
                if can_plant[0]:
                    当前单元格状态[can_plant[2]][can_plant[1]] = 1  # 注意XY颠倒
                    if event.key == pygame.K_1:  # 按下1键,生成豌豆射手
                        if 阳光够吗('豌豆射手'):
                            pygame.mixer.Sound('resource/audio/plant/种下植物.ogg').play()
                            X, Y = 绘制植物(mx, my, '豌豆射手')
                            豌豆射手List.append((summon_plant_class('豌豆射手', X, Y), (X, Y)))
                        else:
                            continue

                    if event.key == pygame.K_2:  # 按下2键,生成西瓜投手
                        if 阳光够吗('西瓜投手'):
                            pygame.mixer.Sound('resource/audio/plant/种下植物.ogg').play()
                            X, Y = 绘制植物(mx, my, '西瓜投手')
                            西瓜投手List.append((summon_plant_class('西瓜投手', X, Y), (X, Y)))
                        else:
                            continue

                    if event.key == pygame.K_3:  # 按下3键,生成玉米加农炮
                        if 阳光够吗('玉米加农炮'):
                            pygame.mixer.Sound('resource/audio/plant/种下植物.ogg').play()
                            X, Y = 绘制植物(mx, my, '玉米加农炮')
                            玉米加农炮List.append((summon_plant_class('玉米加农炮', X, Y), (X, Y)))
                        else:
                            continue

                    if event.key == pygame.K_4:  # 按下4键,生成向日葵(被动)
                        if 阳光够吗('向日葵'):
                            pygame.mixer.Sound('resource/audio/plant/种下植物.ogg').play()
                            X, Y = 绘制植物(mx, my, '向日葵')
                            向日葵List.append((summon_plant_class('向日葵', X, Y), (X, Y)))
                        else:
                            continue

                    pygame.draw.rect(screen, (255, 255, 255), (15, 55, 50, 30), 0)
                    screen.blit(绑定阳光(), (20, 55))
                else:
                    pygame.mixer.Sound('resource/audio/event/否定.ogg').play()
                    continue

            if event.type == TimeCycle:  # 10秒更新僵尸列表和阳光数值
                被动更新阳光()
                生成僵尸()

            if event.type == 玉米攻击周期:  # 12秒通知玉米加农炮new玉米
                同步攻击计数器(玉米加农炮List, 玉米group)

            if event.type == 西瓜攻击周期:  # 4秒通知西瓜投手new西瓜
                同步攻击计数器(西瓜投手List, 西瓜group)

            if event.type == 豌豆攻击周期:  # 3秒通知豌豆射手new豌豆
                同步攻击计数器(豌豆射手List, 豌豆group)

            if event.type == 单位时刻更新:  # 每一秒让僵尸和基础子弹豌豆移动, 并且检测碰撞
                僵尸一键更新(僵尸Group)
                超级投掷物更新(投掷物Group, 僵尸Group)

        pygame.display.flip()

    if 胜利 == 0:
        失败退出(screen)
    else:
        胜利退出(screen)


