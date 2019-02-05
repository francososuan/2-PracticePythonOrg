name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
times = int(input("Please enter number of times of message: "))

time_age = 100 - age

for message in range(0,times):
    print("Hi " + name + ", you will turn 100 after {0} years" .format(time_age))


