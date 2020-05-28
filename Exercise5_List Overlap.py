a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ListA = []
for bb in b:
    if bb in a:
        ListA.append(bb)
print(ListA)


# 2nd part
import random
a = [random.randint(1,10) for i in range(10)]
b = [random.randint(1,10) for i in range(10)]
print(a)
print(b)

ListB = []
for element in a and b:
    if element in a and b:
        ListB.append(element)
print(ListB)

# 3rd part

a = [random.randint(1,10) for i in range(10)]
b = [random.randint(1,10) for i in range(10)]

print(a)
print(b)
ListC = [element for element in a and b if element in a and b]
print(ListC)