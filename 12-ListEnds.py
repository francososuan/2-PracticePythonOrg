import random

a = random.sample(range(100),random.randint(1,100))
#creates a random list of length 1-100 from numbers 1-100

b =[]

b.append(a[0])
b.append(a[-1])

print(a)
print(b)

