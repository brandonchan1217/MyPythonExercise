Fnumber = int(input("please input the number of Fibonnaci numer:"))
count = 0
ini = 0
element = 0

while Fnumber > 1:
    n1 = 0
    n2 = 1

    fibo = [0, 1]
    n1 = n2
    n2 = n1 +n2
    fibo.append(n2)
    Fnumber -= 1

print(fibo)

