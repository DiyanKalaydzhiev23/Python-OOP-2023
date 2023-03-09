class ClassIdMixin:

    @classmethod
    def get_next_id(cls):
        cls.id += 1

        return cls.id
