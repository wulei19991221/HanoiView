# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年11月30日18时
# @File: HanoiView.py
import time
import turtle as t
from pillar import Pillar
from threading import Thread
from queue import Queue
from rect import Rect


class HanoiViewer:
    screen = t.Screen()
    pillarName = ('A', 'B', 'C')
    WIDTH = 800
    HEIGHT = 600
    pillarQueue = Queue(maxsize=3)
    __pillarList = []

    def __init__(self, n: int):
        self.num = n
        self.setScreen()
        self.putPillar()
        self.threadsOfDraw()
        self.drawPlate()

    # 初始化屏幕
    def setScreen(self):
        self.screen.bgcolor('#95a5a6')
        self.screen.title('汉诺塔')
        self.screen.setup(self.WIDTH, self.HEIGHT)
        # 更改常用坐标系, 以屏幕左上角为原点
        self.screen.setworldcoordinates(0, self.HEIGHT, self.WIDTH, 0)

    def drawThreePillar(self):
        while not self.pillarQueue.empty():
            p = self.pillarQueue.get()
            self.__pillarList.append(p)
            p.draw()

    def putPillar(self):
        x_y_list = self.getXAndYList()
        index = 0
        for x, y, width in x_y_list:
            p = Pillar(t.Pen(), x, y, width, self.pillarName[index])
            index += 1
            self.pillarQueue.put(p)

    def getXAndYList(self):
        x_y_list = []
        y = self.HEIGHT - 100
        width = 0
        availabilityZone = self.WIDTH - 200
        single_width = availabilityZone // 3 - 50
        space = (self.WIDTH - 200 - single_width * 3) // 2
        for _ in range(3):
            x_y_list.append((100 + width, y, single_width))
            width += single_width + space
        return x_y_list

    def show(self):
        self.screen.mainloop()

    def threadsOfDraw(self):
        for _ in range(3):
            td = Thread(target=self.drawThreePillar)
            td.start()
        # time.sleep(3)

    def drawPlate(self):
        rect_A = Rect(self.__pillarList[0])
        rect_A.drawRect()


if __name__ == '__main__':
    view = HanoiViewer(1)
    view.show()
