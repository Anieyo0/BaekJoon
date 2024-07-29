n = int(input())

length = len(str(n))

for i in range(1, n + 1):
    gen = sum(map(int, str(i)))
    
    if n == gen + i:
        print(i)
        break
    
    if i == n:
        print('0')