st = input("Enter any mixed case string : \t")

low = 0
up = 0
n = 0
for i in st:
    if i.islower():
        low = low + 1
    elif i.isupper():
        up = up + 1
    else:
        n = n + 1

print("Lower cased characters : ", low)
print("Upper cased characters : ", up)
print("Neutral characters     : ", n)
