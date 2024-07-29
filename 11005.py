CONVERT = {i: i for i in range(10)}
CONVERT.update({index: chr(value) for index, value in enumerate(range(ord('A'), ord('Z') + 1), start=10)})

N, B = map(int, input().split())

N_to_B = []
while True:
    try:
            if N != 0:
                N_to_B.append(N % B)
                N //= B

            else:
                N_to_B.reverse()
                break
    except:
          print('except')
    
for i in range(len(N_to_B)):
    N_to_B[i] = CONVERT[N_to_B[i]]

for i in N_to_B:
     print(i, end='')