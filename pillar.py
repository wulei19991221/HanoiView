# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年11月30日20时
# @File: pillar.py
import turtle as t
from random import choice


class Pillar:
    colors = ('#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#e67e22', '#2c3e50')
    __height = 400
    __width = 150

    def __init__(self, pen: t.Pen, x: int, y: int, width: int, name: str):
        self.__pen = pen
        self.x = x
        self.y = y
        self.__width = width
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

    def home(self):
        self.__pen.goto(self.x, self.y)

    def getColor(self):
        return choice(self.colors)

    def draw(self):
        self.__pen.forward(self.__width)
        self.__pen.backward(self.__width // 2)
        self.__pen.right(90)
        self.__pen.forward(self.__height)
        self.__pen.up()
        self.__pen.goto(self.x + self.__width // 2, self.y + 50)
        self.__pen.down()
        self.__pen.color(self.getColor())
        self.__pen.write(self.name, align='center', font=('Arial', 18, 'normal'))

    def getCenterPosition(self):
        return self.x + self.__width // 2, self.y
