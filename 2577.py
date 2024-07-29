N = 3
result = []

num = []
for _ in range(N):
    num.append(int(input()))

mat = 1
for i in num:
    mat *= i

mat = list(str(mat))

for i in range(10):
    result.append(mat.count(str(i)))

for i in result:
    print(i)