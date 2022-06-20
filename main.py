from box_file import Box, Box_Generater
from rect_file import Rect, Section

BOX_COUNT = 3


def main():
    print("Section (l, b, t, r), [x, y]")
    section = Section(Box(4, 7))
    print(section.to_string())

    gen = Box_Generater()
    boxes = gen.create(BOX_COUNT)

    print("BOX (x, y)")
    for index, box in enumerate(boxes):
        print("[" + str(index) + "] " + box.to_string())


if __name__ == "__main__":
    main()
