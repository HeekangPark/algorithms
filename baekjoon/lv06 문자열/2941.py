c_letters = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

def parse_single_letter(string):
    for c_letter in c_letters:
        if string.startswith(c_letter):
            return string[len(c_letter):]
    return string[1:]

a = input()
word_count = 0
while True:
    a = parse_single_letter(a)
    word_count += 1
    if len(a) == 0:
        break

print(word_count)