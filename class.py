class Base:
    no = 0
    name = None

    def info(self):
        self.no = int(input("Enter your Enrollment number : "))
        self.name = input("Enter your Name              : ")


class Derived:
    marks = 0
    total_marks = 500
    percentage = 0.0

    def get_percentage(self):
        self.marks = int(input("Enter your total marks :- \t"))
        self.percentage = (self.marks*100)/500


class Show(Base, Derived):
    def show_info(self):
        print("\nName              : ", self.name)
        print("Enrollment Number : ", self.no)
        print("Total Marks       : ", self.marks, "/", self.total_marks)
        print("Percentages       : ", self.percentage, "%")


s = Show()
s.info()
s.get_percentage()
s.show_info()
