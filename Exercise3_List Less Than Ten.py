ListA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ListB = []
for element in ListA:
    if element <= 5:
        ListB.append(element)
print(ListB)
# Write in one line
ListC = [aa for aa in ListA if aa < 5]
print(ListC)

# Input a number
numberA = int(input("Please input a number:"))
print([bb for bb in ListA if bb < numberA])