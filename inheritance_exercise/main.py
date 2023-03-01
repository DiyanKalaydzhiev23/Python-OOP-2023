class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_hi(self) -> None:
        print(f"Hi, my name is {self.name}")


class Employee(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def work(self) -> None:
        print(f"Working...")


class Boss(Person):
    pass


class Manager(Employee):
    pass


class Father:
    def __init__(self, name):
        self.name = name


class Mother:
    def __init__(self, name):
        self.name = name


class Child(Father, Mother):
    pass
    # def __init__(self):
    #     Father.__init__()
    #     Mother.__init__()


employee = Employee("Ivan", 30, "programmer")

print(Manager.mro())

employee.say_hi()
employee.work()
print(employee.position)