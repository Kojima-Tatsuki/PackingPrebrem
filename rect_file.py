
from math import fabs
import re
from box_file import Box


class Rect:
    """ 座標を持つ箱 """
    left: int
    right: int
    top: int
    bottom: int

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def area(self) -> int:
        return self.width * self.height

    def __init__(self, left, right, top, bottom):
        if right - left < 0 or top - bottom < 0:
            raise Exception("幅または高さが負の図形の生成を試みました")

        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def __init__(self, box: Box):
        self.left = 0
        self.right = box.width
        self.top = box.height
        self.bottom = 0

    def to_string(self) -> str:
        return "[" + str(self.left) + ", " + str(self.right) + ", " + \
            str(self.top) + ", " + str(self.bottom) + "]," + \
            "[" + str(self.width) + ", " + str(self.height) + "]"


class Space():
    rect: Rect

    def __init__(self, rect: Rect) -> None:
        self.rect = rect

class Section(Rect):
    spaces: list[Space]
    
    def __init__(self, size: Box):
        super().__init__(size)
        self.spaces = list()
        self.spaces.append(Space(size))

    def appendable(box: Box):
        return False
