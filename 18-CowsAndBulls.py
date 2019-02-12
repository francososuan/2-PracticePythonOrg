import random


password = str(random.randint(1000,9999))
print(password)
password_list = [int(d) for d in str(password)]
print(password_list)
while True:
    cow = 0
    bull = 0
    guess = str(input("Please guess the 4 digit password "))
    guess_list = [int(d) for d in str(guess)]
    print(guess_list)
    for num in range(0,4):
        if guess_list[num] == password_list[num]:
            cow = cow +1

        if guess[num] in password and guess_list[num] != password_list[num]:
            bull = bull+1

    if password == int(guess):
        print("Congratulations the password was: " + str(password))
        break

    else:
        print("Cow = " + str(cow))
        print("Bull = " + str(bull))
        print("Try Again")



