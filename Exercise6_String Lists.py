Value = str(input("Please input a string:"))
if Value.lower() == Value[::-1].lower():
    print("{} is a palindrome!".format(Value))
else:
    print("{} is not a palindrome!".format(Value))