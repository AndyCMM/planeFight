# coding=utf-8
# @Time  :2019-03-05 21:00
# @Author:AndyMing
# @File  :plane_sprites.py

import pygame as py


class GameSprite(py.sprite.Sprite):
    """游戏精灵类"""
    def __init__(self, image, speed=1):
        super().__init__()
        # 图像加载
        self.image = py.image.load(image)
        # 图像尺寸
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed

    def update(self, *args):
        # 记录图像移动
        self.rect.y += self.speed


if __name__ == '__main__':
    class C:
        s = None

        def __new__(cls, *args, **kwargs):
            print('{0}'.format('I am new'))
            return super().__new__(cls)

        def __init__(self):
            print('I am init')
            super().__init__()

print(id(C()))

