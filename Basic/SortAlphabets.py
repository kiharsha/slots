def sortAlpha(sentence):
    words = sentence.split()
    words.sort()
    return words

sentence1 = input("Enter a sentence")
print(sortAlpha(sentence1))
