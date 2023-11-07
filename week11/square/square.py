from rectangle import Rectangle
# Implement the Square class
# inharets from rectangel


class Square(Rectangle):
    def __init__(self, side) -> None:
        Rectangle.__init__(self, side, side)
