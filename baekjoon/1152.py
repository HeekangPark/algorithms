string = input()
print(len([word for word in string.strip().split() if len(word) != 0]))