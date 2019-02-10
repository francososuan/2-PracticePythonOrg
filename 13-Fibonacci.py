def fibonacci(length):
    a = 0
    b = 1
    c=[]
    for i in range(1,length+1):
        if i % 2 == 0:
            c.append(b)
            b=a+b
        else:
            c.append(a)
            a = a+b


    return c


length = int(input("Please enter the length of the fibonacci sequence: "))

print(fibonacci(length))