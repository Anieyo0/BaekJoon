import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

# 누적합 계산
cumulative_sum = [0]

for num in nums:
    cumulative_sum.append(cumulative_sum[-1] + num)

# 구간합 구하기
for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    
    print(cumulative_sum[j] - cumulative_sum[i-1])