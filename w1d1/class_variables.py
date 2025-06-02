class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@company.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        print(f"{self.first} {self.last}")
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
print(emp_2.__dict__)
#print(Employee.__dict__)
print(Employee.num_of_emps)

emp_3 = Employee('Steve', 'Veltkamp', 100000)

print(Employee.num_of_emps)