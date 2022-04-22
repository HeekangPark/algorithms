word = input()
print(' '.join([str(word.find(chr(x + ord('a')))) for x in range(26)]))