number = int(input("Please input number: "))

divisor = []

for num in range(1,number+1):
    if number % num  == 0:
        divisor.append(num)

print(divisor)