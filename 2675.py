ITER = int(input())

for _ in  range(ITER):
    iter, str = input().split()
    iter = int(iter)

    for i in range(len(str)):
        print(str[i] * iter, end='')
    print('')