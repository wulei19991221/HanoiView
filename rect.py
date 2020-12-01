# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年12月01日09时
# @File: rect.py
from pillar import Pillar


class Rect:
    colors = Pillar.colors

    def __init__(self, pillar: Pillar):
        # 柱子
        self.pillar = pillar
        self.center_x, self.center_y = self.pillar.getCenterPosition()
        self.max_width, self.max_height = self.pillar.getWidthHeight()
        self.pen = self.pillar.getPen()

    def drawRect(self):
        print('plate')
        self.pillar.toCenter()
        self.pen.color(self.pillar.getColor())
        self.pen.forward(self.max_width // 2)
