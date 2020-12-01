# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年12月01日09时
# @File: rect.py
from pillar import Pillar
import turtle as t


class Plate:
    __pen = t.Pen()
    __pen.hideturtle()

    def __init__(self, pillar: Pillar, width: int):
        # 柱子
        self.pillar = pillar
        self.initPen()
        self.center_x, self.center_y = self.pillar.getCenterPosition()
        self.width = width
        self.height = self.center_y
        # 盘子左端点位置
        self.leftPosition = self.center_x - self.width // 2

    def initPen(self):
        self.__pen.color(self.pillar.getColor())
        self.__pen.speed(6)
        self.__pen.pensize(30)

    # 画盘子
    def drawRect(self):
        self.__pen.up()
        self.__pen.goto(self.leftPosition, self.height)
        self.__pen.down()
        self.__pen.setheading(0)
        self.__pen.forward(self.width)
        self.pillar.width -= 20
        self.pillar.center_y -= 30
