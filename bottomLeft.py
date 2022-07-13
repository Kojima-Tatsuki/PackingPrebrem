from turtle import pu
from box_file import Box
from rect_file import Point, Rect, Section


class BLStablePoint:
    """ BL安定点 """
    __MotherRect: Rect
    """ 母材 """

    __PushedBoxes: list[Rect]
    """ 設置済みの箱のリスト """

    def __init__(self, motherRect, pushedBoxes):
        self.__MotherRect = motherRect
        self.__PushedBoxes = pushedBoxes


class ButtonLeftAlgolism:
    """ BLのアルゴリズム """

    MotherSection: Section
    """ 母材 """

    Rects: list[Box]
    """ 設置する箱のリスト """

    PushedBoxes: list[Rect]
    """ 設置済みの箱のリスト """

    def __init__(self, motherBox: Section, rects: list[Box]) -> None:
        """ rectsの順に設置する """
        self.MotherSection = Section(motherBox)
        self.Rects = list(rects)
        self.PushedBoxes = list()

    def Cal(self):
        """ 計算したスコアを返す """
        for rect in self.Rects:
            stablePoints = self.__GetBLStablePoints()
            if len(stablePoints) == 0:
                break
            stablePoints: list[Point] = self.__SortList(stablePoints)
            for p in stablePoints:
                rect = Rect(p.x, p.x + rect.width, p.y + rect.height, p.y)

                if self.MotherSection.IsAppendable(rect) is False:
                    # print("Mother Block")
                    continue

                if self.__IsOverlapPushed(rect):
                    # print("Overlap")
                    continue

                self.__PushRect(rect)
                # print("Pushed {}".format(rect.to_string()))
                break

        return self.PushedBoxes

    def __PushRect(self, rect: Rect) -> None:
        """ 箱を追加する """
        self.PushedBoxes.append(rect)

    def __Pushable(self, rect: Rect) -> bool:
        """ 制約条件を満たすかを返す, 新たに箱が追加できるかを返す"""
        return False

    def __GetBLStablePoints(self) -> list[Point]:
        """ 設置可能なBL安定点を返す """

        result = list[Point]()

        self.__AppendPoint(result, Point(self.MotherSection.left, self.MotherSection.bottom))

        for pushed in self.PushedBoxes:
            self.__AppendPoint(result, Point(pushed.right, self.MotherSection.bottom))
            self.__AppendPoint(result, Point(self.MotherSection.left, pushed.top))

            for repushed in self.PushedBoxes:
                if repushed.Equals(pushed):  # 同じものならスキップ
                    continue

                if (pushed.top >= repushed.top):
                    self.__AppendPoint(result, Point(pushed.right, repushed.top))

                if (pushed.right >= repushed.right):
                    self.__AppendPoint(result, Point(repushed.right, pushed.top))

        return result

    def __IsOverlapPushed(self, rect: Rect):
        """ 既に設置済みの箱と重なっているかを返す """
        for pushed in self.PushedBoxes:
            if self.__IsOverlap(rect, pushed):
                return True
        return False

    def __IsOverlap(self, a: Rect, b: Rect) -> bool:
        """ AとBが重なっているかを返す """
        # if a.IsOverlap(Point(b.left, b.bottom) or b.IsOverlap(Point(a.left, a.bottom))):
        #     return True
        # if a.IsOverlap(Point(b.left, b.top)) or b.IsOverlap(Point(a.left, a.top)):
        #     return True
        # if a.IsOverlap(Point(b.right, b.bottom)) or b.IsOverlap(Point(a.right, a.bottom)):
        #     return True
        # if a.IsOverlap(Point(b.right, b.top)) or b.IsOverlap(Point(a.right, a.top)):
        #     return True
        # return False
        return a.IsOverlapRect(b)

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
        result: int = self.MotherSection.bottom
        for pushed in self.PushedBoxes:
            if result < pushed.top:
                result = pushed.top
        return result

    def __SortList(self, list: list[Point]) -> list[Point]:
        """ 高さ、横順に並び変える """
        # result = sorted(result, key=lambda x: x.x)
        result = sorted(list, key=lambda x: x.y)
        # print("stable")
        # for p in result:
        #     print(p.to_string())
        return result
