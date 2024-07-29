size = int(input())
nums = list(map(int, input().split()))

dist_list = []  # 오르막길 길이를 저장하기 위한 변수
dist = 0    
for i in range(size-1):
    
    if nums[i] < nums[i+1]: # 오르막이 끊기지 않는 경우
        dist += nums[i+1] - nums[i]
        dist_list.append(dist)
        
    else:   # 오르막이 끊긴 경우
        dist_list.append(dist)
        dist = 0
        
print(max(dist_list))