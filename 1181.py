N = int(input())

nums = []
for i in range(N):
    nums.append(input())
    
nums = list(set(nums))
nums.sort()
nums.sort(key = len)

for num in nums:
    print(num)