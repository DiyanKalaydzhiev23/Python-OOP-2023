class CreditCard:
    def __init__(self, number: str, holder_name: str, cvv: str, expr_date: str, pin: str):
        self._number = number  # protected
        self.holder_name = holder_name
        self.cvv = cvv
        self.expr_date = expr_date
        self.__pin = pin # private

    # def get_pin(self):
    #     return self.__pin


class OnlineCreditCard(CreditCard):
    def __init__(self, number: str, holder_name: str, cvv: str, expr_date: str, pin: str):
        super().__init__(number, holder_name, cvv, expr_date, pin)


visa = CreditCard("5761357435421", "Test name", "123", "10/10/2020", "1111")
print(visa._CreditCard__pin)