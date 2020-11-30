import random

class LabAssistants:
    def isokay(self):
        return "yes" if input("Are all components okay?(y/n)") else "no"


class Staff:



class Hod(Staff):




class Principal(LabAssistants, Hod):
    def purchasing(self):
        if self.isokay() == "no":
            sys_no = int(input("How many System do you want to buy ?"))
            random.randrange(10000, 99999)
            for i in range(sys_no):



    def exam(self):

