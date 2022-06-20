from box_file import Box
from rect_file import Rect, Section

class ButtonLeftAlgolism:
    """ BLのアルゴリズム """
    Rects: list[Rect]
    """ 設置する箱のリスト """

    def __init__(self) -> None:
        self.Rects = list[Rect]()

    def __PushRect(self, rect: Rect) -> None:
        self.Rects.append(rect)

    def __Pushable(self, rect: Rect) -> bool:
        """ 制約条件 """
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

