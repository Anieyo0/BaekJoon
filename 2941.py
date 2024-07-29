CROATIA_ALPHABET = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = input()

for word in CROATIA_ALPHABET:
    str = str.replace(word, '*')

print(len(str))