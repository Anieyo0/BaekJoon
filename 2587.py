nums = []

for _ in range(5):
    nums.append(int(input()))
    
nums.sort()
    
print(int(sum(nums) / len(nums))) # 평균
print(nums[len(nums) // 2])