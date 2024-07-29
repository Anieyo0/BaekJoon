import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
X = int(sys.stdin.readline().rstrip())

nums.sort()

i = 0
j = N - 1
cnt = 0
while i < j:
    if nums[i] + nums[j] == X:
        cnt += 1
        i += 1
        j -= 1
        
    elif nums[i] + nums[j] > X:
        j -= 1
        
    else:
        i += 1
        
print(cnt)
        
