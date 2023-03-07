class Employee:
    name = 'Diyan'
    salary = '25000'

    def __getattribute__(self, attr):
        return None

    def show(self):
        print(self.name)
        print(self.salary)


employee = Employee()
print(employee.name)

a = 5
