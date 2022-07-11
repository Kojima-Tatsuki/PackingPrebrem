from box_file import Box
from rect_file import Rect, Section

class ButtonLeftAlgolism:
    """ BLのアルゴリズム """
    Rects: list[Rect]
    """ 設置する箱のリスト """

    PushedBoxes: list[Rect]

    def __init__(self, rects: list[Rect]) -> None:
        """ rectsの順に設置する """
        self.Rects = list(rects)

    def Cal(self) -> int:
        """ 計算したスコアを返す """
        return

    def __PushRect(self, rect: Rect) -> None:
        """ 箱を追加する """
        self.Rects.append(rect)

    def __Pushable(self, rect: Rect) -> bool:
        """ 制約条件を満たすかを返す, 新たに箱が追加できるかを返す"""
        return False

    def __IsOverlap(a: Rect, b: Rect) -> bool:
        if a.left + a.width > b.left:
            return True
        if a.bottom + a.height > b.top:
            return True
        if b.left + b.width > a.left:
            return True
        if b.bottom + b.height > a.top:
            return True
        return False

