from animal import Animal


class Prey(Animal):
    number_of_ofsprings = 2

    def __init__(self, island, x=0, y=0, name="O"):
        super().__init__(island, x, y, name)
        # or Animal.__init__(self, island, x, y, name)
