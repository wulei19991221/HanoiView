# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年11月30日20时
# @File: pillar.py
import turtle as t
from random import choice


class Pillar:
    # 柱子颜色
    colors = ('#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#e67e22', '#2c3e50')
    # 柱子宽度和高度
    __height = 400
    __width = 150
    center_x = 0
    center_y = __height

    def __init__(self, pen: t.Pen, x: int, y: int, width: int, name: str):
        self.__pen = pen
        self.x = x
        self.y = y
        self.__width = width
        self.center_x = self.x + self.__width // 2
        self.center_y = self.y
        self.name = name
        self.initPen()

    def initPen(self):
        self.__pen.hideturtle()
        self.__pen.speed(5)
        self.__pen.color(self.getColor())
        self.__pen.pensize(3)
        self.__pen.up()
        self.__pen.goto(self.x, self.y)
        self.__pen.down()

    def toCenter(self):
        self.__pen.up()
        self.__pen.goto(self.center_x, self.center_y)
        self.__pen.down()

    # 返回随机颜色代码
    def getColor(self):
        return choice(self.colors)

    # 画柱子
    def draw(self):
        # 画底盘
        self.__pen.forward(self.__width)
        self.toCenter()
        # 画支柱
        self.__pen.right(90)
        self.__pen.forward(self.__height)
        self.toCenter()
        # 画字母
        self.__pen.forward(-50)
        self.__pen.color(self.getColor())
        self.__pen.write(self.name, align='center', font=('Arial', 18, 'normal'))

    # 返回柱子底部中心坐标
    def getCenterPosition(self):
        return self.center_x, self.center_y
