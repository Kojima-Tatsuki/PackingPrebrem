from hashlib import new
from box_file import Box
from rect_file import Rect, Section

class DoughnutAlgolism:
    """ ドーナツ型のアルゴリズム """
    Rects: list[Rect]
    """ 設置する箱のリスト """

    def __init__(self) -> None:
        self.Rects = list[Rect]()

    def __PushRect(self, rect: Rect) -> None:
        self.Rects.append(rect)


