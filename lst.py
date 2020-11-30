ls = [1, 2, 4, 5]
print("List         : ", ls)

ls.insert(2, 3)
print("List insert  : ", ls)

ls.append(6)
print("List append  : ", ls)

ls1 = ls.copy()
print("List copy    : ", ls1)

ls.pop()
print("List POP     : ", ls)

print("List slicing : ", ls[1:2])

ls.sort()
print("List sort    : ", ls)

ls.remove(5)
print("List remove  : ", ls)

ls.reverse()
print("List reverse : ", ls)

print("List length  : ", ls.__len__())

print("List index   : ", ls.index(3))

print("List Concat  :", ls.__add__([7, 8, 9]))

print("Contains 3 ?  :", ls.__contains__(3))

ls.clear()
print("List cleared : ", ls)
