class Teacher:
    teacher_info_lst = []
    qualify = ""
    name = ""
    subject = ""
    experience = 0

    def teacher_info(self):
        self.name = input("Enter your Name       : ")
        self.subject = input("Enter your Subject    : ")
        self.experience = input("Enter your Experience : ")
        self.qualify = input("Enter your Qualification : ")
        self.teacher_info_lst.append([self.subject, self.name, self.experience, self.qualify])


class HOD(Teacher):
    def assign_teacher(self):
        max_exp = []
        sub = input("For which subject do you want a teacher ?\n")
        for i in self.teacher_info_lst:
            if self.teacher_info_lst[i].__contains__(sub):
                max_exp.append(self.teacher_info_lst[i][2])
                print("Experience of ", self.teacher_info_lst[i][1], " is ", self.teacher_info_lst[i][2], " in ",
                      self.teacher_info_lst[i][0])

        copy_max = max_exp
        max_exp.sort()
        exp = max_exp[max_exp.__len__() - 1]


class Principal:
    price = []
    fund = 0

    def tender(self):
        tend = int(input("How many Tenders are there ?\n"))
        for i in range(tend):
            self.price.append(int(input("Enter price of tender ")))

    def get_fund(self):
        self.fund = int(input("Enter your available Fund : "))

    def check_tender(self):
        self.price.sort()
        if self.price[0] < self.fund:
            print("The tender selected is pricing Rs. ", self.price[0])
            print("The remaining Fund is ", self.fund - self.price[0])
