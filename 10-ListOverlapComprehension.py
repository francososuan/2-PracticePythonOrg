import random

a = random.sample(range(100),random.randint(1,100))
b= random.sample(range(100),random.randint(1,100))


print(a)
print(b)

c = [num for num in a if num in b]

print(c)
