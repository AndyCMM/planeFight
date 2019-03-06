# coding=utf-8
# @Time  :2019-03-04 21:11
# @Author:AndyMing
# @File  :hm_01_pygame.py

import pygame as py
from plane_sprites import GameSprite as GS

bg = py.image.load("./images/background.png")
hero = py.image.load("./images/me1.png")
print(hero.get_rect())
# 游戏初始化
py.init()
clock = py.time.Clock()
# game body
# 绘制背景图片
screen = py.display.set_mode((480, 700))
# 绘制英雄的图片
hero_rec = py.Rect(150, 500, 102, 126)
# 绘制敌机精灵
enemy1 = GS("./images/enemy1.png")
enemy2 = GS("./images/enemy2.png")
enemy2.rect.x = 200
enemy_group = py.sprite.Group(enemy1, enemy2)

while True:
    clock.tick(60)
    #event = py.event.get()
    for event in py.event.get():
       # print(type(event.type))
        if event.type == py.QUIT:
            print('我退出了')
            py.quit()
            exit()
    screen.blit(bg, (0, 0))
    hero_rec.y -= 1
    if hero_rec.y + hero_rec.height < 0:
        hero_rec.y = 700
    screen.blit(hero, hero_rec)
    enemy_group.update()
    enemy_group.draw(screen)
    py.display.update()
# game over
# py.quit()



