# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年11月30日18时
# @File: HanoiView.py
import turtle as t
from pillar import Pillar
from rect import Plate


class HanoiViewer:
    screen = t.Screen()
    pillarName = ('A', 'B', 'C')
    WIDTH = 800
    HEIGHT = 600
    __pillarList = []

    def __init__(self, n: int):
        self.num = n
        self.setScreen()
        self.putPillar()
        self.drawThreePillar()
        self.drawPlate()

    # 初始化屏幕
    def setScreen(self):
        self.screen.bgcolor('black')
        self.screen.title('汉诺塔')
        self.screen.setup(self.WIDTH, self.HEIGHT)
        # 更改常用坐标系, 以屏幕左上角为原点
        self.screen.setworldcoordinates(0, self.HEIGHT, self.WIDTH, 0)

    # 放柱子
    def putPillar(self):
        x_y_list = self.getXAndYList()
        index = 0
        for x, y, width in x_y_list:
            p = Pillar(t.Pen(), x, y, width, self.pillarName[index])
            index += 1
            self.__pillarList.append(p)

    # 画柱子
    def drawThreePillar(self):
        for p in self.__pillarList:
            p.draw()

    # 获取x,y,和 柱子的底盘宽度
    def getXAndYList(self):
        x_y_list = []
        # y的坐标
        y = self.HEIGHT - 100
        width = 0
        # 去除左右留下的各100的空间
        availabilityZone = self.WIDTH - 200
        # 单个柱子所占宽度
        single_width = availabilityZone // 3 - 50
        # 柱子之间的空间, |---1--2--3---|, 200 + 2 * space + 3 * single_width = self.WIDTH
        space = (self.WIDTH - 200 - single_width * 3) // 2
        for _ in range(3):
            x_y_list.append((100 + width, y, single_width))
            width += single_width + space
        return x_y_list

    # 屏幕显示
    def show(self):
        self.screen.mainloop()

    def drawPlate(self):
        a_pillar = self.__pillarList[0]
        for i in range(self.num):
            plate = Plate(a_pillar, a_pillar.width)
            plate.drawRect()


if __name__ == '__main__':
    view = HanoiViewer(3)
    view.show()
