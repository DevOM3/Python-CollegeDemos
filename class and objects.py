class Employee:
    id = 1234
    name = "Om Londhe"
    address = "xyz-123-aurangabad"
    salary = 0.0

    def take_input(self):
        self.id = int(input("\n\nEnter your Employee ID   : "))
        self.name = input("Enter your Name          : ")
        self.address = input("Enter your Address       : ")
        self.salary = int(input("Enter your Salary        : "))

    def show_info(self):
        print("\nEmployee ID      : ", self.id)
        print("Employee Name    : ", self.name)
        print("Employee Address : ", self.address)
        print("Employee Salary  : ", self.salary)

    # def check_sal(self):
    #     if self.salary


e = Employee()
e.show_info()
e.take_input()
e.show_info()
