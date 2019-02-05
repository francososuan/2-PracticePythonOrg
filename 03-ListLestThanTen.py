a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b =[]

less_than = int(input("Please enter number lower than: " ))

for item in a:
    if item < less_than:
        b.append(item)


print(b)