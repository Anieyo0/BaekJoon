a = int(input())
b = int(input())

sum = 0
prime = []
for num in range(a, b + 1):
    is_prime = True
    
    if num < 2:
        continue
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            
    if is_prime:
        sum += num
        prime.append(num)
        
prime.sort()

if len(prime) == 0:
    print('-1')

else:
    print(sum)
    print(prime[0])