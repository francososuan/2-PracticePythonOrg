number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("The number {0} is Even" .format(number))

else:
    print("The number {0} is Odd".format(number))


num = int(input("Please enter first number: "))
check = int(input("Please enter second number: "))

if num % check ==0:
    print("{0} is divisible by {1}".format(num,check))
else:
    print("{0} is not divisible by {1}".format(num,check))