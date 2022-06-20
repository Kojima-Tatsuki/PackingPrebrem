from random import Random
import random

BOX_SIZE = 5

class Box:
    """ 座標を持たない箱 """
    height: int
    width: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def to_string(self) -> str:
        return "(" + str(self.width) + ", " + str(self.height) + ")"

# box をランダムに生成する


class Box_Generater:
    """ Box class を生成するclass """

    def create(self, count: int) -> list[Box]:
        """
        Parameters
        ----------
        count : int
            生成するBoxの数
        
        Returns
        ----------
        list[Box]
            生成されたBoxのリスト
        """
        result = list[Box]()

        for i in range(count):
            width = random.randint(1, BOX_SIZE)
            height = random.randint(1, BOX_SIZE)
            result.append(Box(width, height))

        return result
