# Implement the Shape class
class Shape:
    def __init__(self, length=0.0, width=0.0) -> None:
        pass

    def __str__(self) -> str:
        return f"{type(self).__name__} with area of {round(self.get_area(),2)} and perimeter of {round(self.get_perimeter(),2)}" # type: ignore
