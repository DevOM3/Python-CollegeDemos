def add(a, b):
    return a+b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


no1 = int(input("Enter a number : "))
no2 = int(input("Enter a number : "))

print("Addition is       ", add(no1, no2))
print("Subtraction is    ", sub(no1, no2))
print("Multiplication is ", mul(no1, no2))
try:
    print("Division is       ", div(no1, no2))
except Exception as e:
    print(e)
