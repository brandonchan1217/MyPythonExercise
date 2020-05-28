
inumber = int(input("please input a number that is greater than 2:"))

def isprime(i):
    count = 0
    for a in range(1,i):
        if i % a == 0:
            count += 1
    if count != 0:
        return 1
def divisor(i):
    ListA = []
    for aa in range(1, i):
        if i % aa != 0:
            ListA.append(aa)
    return ListA

prime = isprime(inumber)
list = divisor(inumber)
if prime:
    print("this is not a prime number and its divisor is",list)