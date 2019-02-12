import string
import random

def pw_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
	return "".join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)