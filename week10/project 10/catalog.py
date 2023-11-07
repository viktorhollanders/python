

class Catalog:
    def __init__(self, name: str) -> None:
        self.name = name
        self.item_list = []

    def set_name(self, new_name: str):
        self.name = new_name

    def add(self, item):
        self.item_list.append(item)

    def remove(self, item):
        self.item_list.remove(item)

    def clear(self):
        self.item_list = []

    def __str__(self) -> str:
        output = f"Catalog {self.name}:"

        for item in self.item_list:
            output += f"\n\t{item}"

        return output



# pass by refrence