class Item:
    def __init__(self, name: str, catagory: str) -> None:
        self.name = name
        self.catagoty = catagory

    def set_name(self, new_name: str):
        self.name = new_name

    def set_category(self, new_catagory: str):
        self.catagoty = new_catagory

    def __str__(self) -> str:
        return f"Name: {self.name}, Category: {self.catagoty}"
