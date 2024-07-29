N = int(input())

nums = list(map(int, input().split()))

count = 0

for num in nums:
    is_prime = True
    
    if num < 2:
        continue
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        count += 1
        
print(count)