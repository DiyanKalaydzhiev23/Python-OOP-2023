from project.class_id_mixin import ClassIdMixin


class Equipment(ClassIdMixin):
    id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
