class Base:
    @staticmethod
    def base():
        print("Hello from base class")


class Derived:
    @staticmethod
    def derived():
        print("Hello from derived class")


class Child(Base, Derived):
    @staticmethod
    def child():
        print("Hello from child class")


c = Child()
c.child()
c.derived()
c.base()
