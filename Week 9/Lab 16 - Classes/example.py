class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return('{} {}'.format(self.first, self.last))

emp1 = Employee('Bearach', 'Byrne', 28000)
emp2 = Employee('Corey', 'Schafer', 40000)

emp1.fullname()
print(Employee.fullname(emp1))
# print(emp1.fullname())
