
from math import fabs
import re
from box_file import Box


class Point:
    """ 2次元座標系での点 """
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self) -> str:
        return "{}, {}".format(self.x, self.y)


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

    def Equals(self, other):
        if (self == other):
            return True
        return False

    def IsOverlap(self, point: Point) -> bool:
        if (self.left < point.x and point.x < self.right and self.top > point.y and point.y > self.bottom):
            return True
        return False

    def IsOverlapRect(self, rect) -> bool:
        return max(self.left, rect.left) < min(self.right, rect.right) and max(self.bottom, rect.bottom) < min(self.top, rect.top)

    def to_string(self) -> str:
        return "[{}, {}], [{}, {}]".format(self.left, self.bottom, self.width, self.height)


class Space():
    rect: Rect

    def __init__(self, rect: Rect) -> None:
        self.rect = rect


class Section(Rect):
    spaces: list[Space]

    def __init__(self, size: Box):
        super().__init__(0, size.width, size.height, 0)
        self.spaces = list()
        self.spaces.append(Space(size))

    def IsAppendable(self, rect: Rect):
        """ 母材の範囲内に存在するか """

        if self.left > rect.left:
            return False
        if self.right < rect.right:
            return False
        if self.bottom > rect.bottom:
            return False
        if self.top < rect.top:
            return False
        return True
