word = str(input("Please input a word "))

if word[::-1] == word:
    print("{} is a palindrome" .format(word))
else:
    print("{} is not a palindrome".format(word))