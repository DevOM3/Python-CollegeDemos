class Base:
    def __init__(self):
        print("Hello from base class Constructor")


class Derived(Base):
    def __init__(self):
        print("Hello from derived class Constructor")


d = Derived()
