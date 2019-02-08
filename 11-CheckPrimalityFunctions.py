def divisors():
    number = int(input("Please input number: "))
    divisor = []

    for num in range(1,number+1):
        if number % num  == 0:
            divisor.append(num)

    return divisor


num = divisors()
if len(num) == 1:
    print("It is a special number")
elif len(num)== 2:
    print("It is a prime number")
else:
    print("It is a composite number")
