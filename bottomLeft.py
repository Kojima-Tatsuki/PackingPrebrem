from turtle import pu
from box_file import Box
from rect_file import Point, Rect, Section


class ButtonLeftAlgolism:
    """ BLのアルゴリズム """

    MotherRect: Section
    """ 母材 """

    Rects: list[Rect]
    """ 設置する箱のリスト """

    PushedBoxes: list[Rect]
    """ 設置済みの箱のリスト """

    def __init__(self, motherBox: Section, rects: list[Rect]) -> None:
        """ rectsの順に設置する """
        self.MotherRect = Section(motherBox)
        self.Rects = list(rects)

    def Cal(self) -> int:
        """ 計算したスコアを返す """
        stablePoints = self.__GetBLStablePoints()

        return self.__GetMaxHeight()

    def __PushRect(self, rect: Rect) -> None:
        """ 箱を追加する """
        self.Rects.append(rect)

    def __Pushable(self, rect: Rect) -> bool:
        """ 制約条件を満たすかを返す, 新たに箱が追加できるかを返す"""
        return False

    def __GetBLStablePoints(self) -> list[Point]:
        """ BL安定点を返す """

        result = list[Point]()

        self.__AppendPoint(result, Point(self.MotherRect.left, self.MotherRect.bottom))

        for pushed in self.PushedBoxes:
            self.__AppendPoint(result, Point(pushed.right, self.MotherRect.bottom))
            self.__AppendPoint(result, Point(self.MotherRect.left, pushed.top))

            for repushed in self.PushedBoxes:
                if repushed.Equals(pushed):  # 同じものならスキップ
                    continue

                if (pushed.top >= repushed.top):
                    self.__AppendPoint(result, Point(pushed.right, repushed.top))

                if (pushed.right >= repushed.right):
                    self.__AppendPoint(result, Point(repushed.right, pushed.top))

        return

    def __IsOverlap(a: Rect, b: Rect) -> bool:
        """ AとBが重なっているかを返す """
        if a.left + a.width > b.left:
            return True
        if a.bottom + a.height > b.top:
            return True
        if b.left + b.width > a.left:
            return True
        if b.bottom + b.height > a.top:
            return True
        return False

    def __AppendPoint(self, appendedList: list[Point], appendPoint: Point) -> bool:
        """ 点が追加可能か追加しても大丈夫かを判定し、追加する """
        # 追加する点に既に箱が存在するか
        if self.__IsFilled(appendPoint):
            return False

        appendedList.append(appendPoint)
        return True

    def __IsFilled(self, point: Point) -> bool:
        """ 指定した点が設置済みの箱のいずれかの内部にあたるを返す """
        for pushed in self.PushedBoxes:
            if pushed.IsOverlap(point):
                return True
        return False

    def __GetMaxHeight(self) -> int:
        """ 設置済みの箱の中で最大の高さにあるものの高さを返す """
        result: int = self.MotherRect.bottom
        for pushed in self.PushedBoxes:
            if result < pushed.top:
                result = pushed.top
        return result


class BLStablePoints:
    __MotherRect: Rect
    """ 母材 """

    __PushedBoxes: list[Rect]
    """ 設置済みの箱のリスト """

    def __init__(self, motherRect, pushedBoxes):
        self.__MotherRect = motherRect
        self.__PushedBoxes = pushedBoxes
