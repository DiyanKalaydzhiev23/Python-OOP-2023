from functools import reduce
from typing import List


class Calculator:

    @staticmethod
    def add(*nums: List[int]) -> int:
        return sum(nums)

    @staticmethod
    def multiply(*nums: List[int]):
        return reduce(lambda a, b: a * b, nums)

    @staticmethod
    def divide(*nums: List[int]):
        return reduce(lambda a, b: a / b, nums)  # a + b if a == 0 or b == 0 else a / b

    @staticmethod
    def subtract(*nums: List[int]):
        return reduce(lambda a, b: a - b, nums)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(70, -50, 43, 7))
