from shape import Shape

# Implement the Rectangle class
# inharets from Shape


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length + self.width) * 2
