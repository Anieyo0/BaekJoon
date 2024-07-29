a = list(map(int, input()))

a.sort()
a = a[::-1]

for i in range(len(a)):
    print(a[i], end='')