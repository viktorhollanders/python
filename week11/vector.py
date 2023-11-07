import math

TOLERANCE = 0.000_000_1


class Vector:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"[[ {self.x} {self.y} {self.z} ]]"

    def __abs__(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other: "Vector") -> bool:
        return abs(self - other) < TOLERANCE

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        return self * scalar

    def __repr__(self) -> str:
        """Returns a parsable string representation of the Vector.

        This means that Python will be able to recreate the object
        from the representation
        when repr() is used in conjunction with functions like eval().
        """

        return f"Vector({self.x}, {self.y}, {self.z})"

    def __gt__(self, other: "Vector") -> bool:
        return abs(self) > abs(other)

    def __ge__(self, other: "Vector") -> bool:
        return abs(self) >= abs(other)

    def __lt__(self, other: "Vector") -> bool:
        return abs(self) < abs(other)

    def __le__(self, other: "Vector") -> bool:
        return abs(self) <= abs(other)

    def dot(self, other: "Vector") -> float:
        dot_x = self.x * other.x
        dot_y = self.y * other.y
        dot_z = self.z * other.z
        return dot_x + dot_y + dot_z

    def cross(self, other: "Vector") -> "Vector":
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x

        return Vector(x, y, z)

