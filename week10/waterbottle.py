class WaterBottle:
    def __init__(self, max_capacity=2.0):
        self.max_capacity = max_capacity
        self.current_contents = 0.0

    def fill(self) -> None:
        self.current_contents = self.max_capacity

    def drink(self, amount: float) -> float:
        if amount < 0:
            return 0
        elif amount >= self.current_contents:
            empty_amount = self.current_contents
            self.current_contents = 0
            return empty_amount
        else:
            self.current_contents -= amount
            return amount

    def __str__(self) -> str:
        return f"The bottle currently holds {self.current_contents:.1f}L of water."
