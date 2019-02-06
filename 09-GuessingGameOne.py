import random

num = random.randint(1,9)
counter = 0

while True:
    guess = int(input("Please guess the number from 1 to 9: "))
    counter = counter + 1

    if num > guess:
        print("Too Low!")
    elif num < guess:
        print("Too High!")
    else:
        print("Congratulations! You have guessed the number! ")
        break


print("Number of guesses: {0}" .format(counter))