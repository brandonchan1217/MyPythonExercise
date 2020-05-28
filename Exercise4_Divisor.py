# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
numberA = int(input("Please input a number:"))
ListA = []
for aa in range(1,numberA):
    if numberA % aa != 0:
        ListA.append(aa)
print(ListA)

