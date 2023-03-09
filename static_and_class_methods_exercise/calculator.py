from collections import deque
from functools import reduce
from typing import List


class Calculator:

    @staticmethod
    def add(*nums: List[int or float]):
        return sum(nums)

    @staticmethod
    def multiply(*nums: List[int or float]):
        return reduce(lambda a, b: a * b, nums)

    @staticmethod
    def divide(*nums: List[int or float]):
        return reduce(lambda a, b: a / b, nums)

    @staticmethod
    def subtract(*nums: List[int or float]):
        return reduce(lambda a, b: a - b, nums)


def custom_reduce(func, elements):
    elements = deque(elements)

    arguments_count = func.__code__.co_argcount

    while len(elements) > 1:
        arguments = [elements.popleft() for _ in range(arguments_count)]
        elements.appendleft(func(*arguments))

    return elements[0]


print(custom_reduce(lambda a, b, c: a * b - c, [1, 2, 3]))