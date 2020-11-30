def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


no1 = int(input("Enter first number                       : "))
sign = input("Enter the operation sign (+ | - | * | /) : ")
no2 = int(input("Enter second number                      : "))

if sign == '+':
    res = addition(no1, no2)
    print("Addition is ", res)
elif sign == '-':
    res = subtraction(no1, no2)
    print("Subtraction is ", res)
elif sign == '*':
    res = multiplication(no1, no2)
    print("Multiplication is ", res)
elif sign == '/':
    res = division(no1, no2)
    print("Division is ", res)
else:
    print("Wrong choice !!!! Try again")
