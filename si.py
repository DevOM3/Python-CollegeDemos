class Person(object):

    # Constructor 
    def __init__(self, name):
        self.name = name

        # To get name

    def getName(self):
        return self.name

        # To check if this person is an employee

    def isEmployee(self):
        return False


class Employee(Person):

    # Here we return true 
    def isEmployee(self):
        return True


# Driver code
emp = Person("One")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Two")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
