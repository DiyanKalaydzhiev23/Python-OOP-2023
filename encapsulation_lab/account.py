class Account:
    def __init__(self, account_id: int, balance: float, pin: int):
        self.__id = account_id
        self.__pin = pin
        self.balance = balance

    def get_id(self, pin: int) -> int or str:
        if pin != self.__pin:
            return "Wrong pin"

        return self.__id

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if old_pin != self.__pin:
            return "Wrong pin"

        self.__pin = new_pin

        return "Pin changed"
