import random
RN = random.randint(1,9)
guess = 0
count = 0

while guess != "exit" and guess != RN:
    guess = input("please guess a number:")
    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < RN:
        print("Your guess is too low!")

    elif guess > RN:
        print("Your guess is too high!")

    else:
        print("Your guess is right!")
        print("It only takes you {} tries".format(count))
