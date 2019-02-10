def reverser(sentence):
    sentence_list = sentence.split(" ")
    reverse_list = []
    for i in range(len(sentence_list)-1,-1,-1):
        reverse_list.append(sentence_list[i])

    return " ".join(reverse_list)


input_sentence = str(input("Please enter a sentence: "))

print(reverser(input_sentence))