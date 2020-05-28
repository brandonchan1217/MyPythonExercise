import random
ListA = [random.randint(1,10) for i in range(10)]
print(ListA)

def decouple_v1(A):
    ListC = []
    for a in A:
        if a not in ListC:
            ListC.append(a)
    return ListC

def decouple_v2(A):
     ListC = set(A)
     return ListC

print(decouple_v1(ListA))
print(decouple_v2(ListA))