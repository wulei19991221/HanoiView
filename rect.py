# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年12月01日09时
# @File: rect.py
from pillar import Pillar
import turtle as t


class Plate:
    pen = t.Pen()
    pen.hideturtle()
    width = 0

    def __init__(self, pillar: Pillar, width: int, name: str):
        self.name = name
        # 柱子
        self.pillar = pillar
        self.initPen()
        self.center_x, self.center_y = self.pillar.getCenterPosition()
        self.width = width
        self.height = self.center_y
        # 盘子左端点位置
        self.leftPosition = self.center_x - self.width // 2

    def initPen(self):
        self.pen.color(self.pillar.getColor())
        self.pen.speed(1)
        self.pen.pensize(30)

    # 画盘子
    def drawRect(self):
        self.__init__(self.pillar, self.width, self.name)
        self.pen.up()
        self.pen.goto(self.leftPosition, self.height)
        self.pen.down()
        self.pen.setheading(0)
        self.pen.color(self.pillar.getColor())
        self.pen.forward(self.width)
        self.pen.up()
        self.pen.goto(self.center_x, self.height + 15)
        self.pen.down()
        self.pen.color('black')
        self.pen.write(self.name, align='center', font=('Arial', 18, 'normal'))
        self.pillar.width -= 20
        self.pillar.center_y -= 30
