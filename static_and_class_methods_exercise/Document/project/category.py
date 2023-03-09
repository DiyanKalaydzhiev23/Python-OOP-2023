class Category:
    def __init__(self, id_number: int, name: str):
        self.id = id_number
        self.name = name

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
