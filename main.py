from pprint import pprint

import numpy as np
from bottomLeft import ButtonLeftAlgolism
from box_file import Box, Box_Generater
from rect_file import Rect, Section

BOX_COUNT = 20


def main():
    print("Section (l, b, t, r), [w, h]")
    section = Section(Box(8, 16))
    print(section.to_string())

    gen = Box_Generater()
    boxes = gen.create(BOX_COUNT)

    print("BOX (w, h)")
    for index, box in enumerate(boxes):
        print("[{}] ".format(index) + box.to_string())

    bl = ButtonLeftAlgolism(section, boxes)

    print("Pushed (l, b, t, r), [w, h]")
    for index, r in enumerate(bl.Cal()):
        print("[{}] {}".format(index, r.to_string()))

    # bl.Cal()


if __name__ == "__main__":
    main()
