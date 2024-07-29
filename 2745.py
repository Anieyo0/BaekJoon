NUMBERS_10 = {chr(i): i - ord('A') + 10 for i in range(ord('A'), ord('Z') + 1)}
NUMBERS_10.update({str(i): i for i in range(10)})

N, B = input().split()

N = list(N)
B = int(B)

N_10 = []
for i in N:
    N_10.append(NUMBERS_10[i])

result = 0
for index, _ in enumerate(N_10):
    power = len(N_10) - index - 1
    result += N_10[index]*(B ** power)

print(result)