nums = list(map(int, input().split()))

for _ in range(4):
    for i in range(4):
        temp = 0    # 교환을 위한 변수
        if nums[i] > nums[i+1]:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
            
            for num in nums:
                print(num, end=' ')
            print()