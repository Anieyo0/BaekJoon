N, M = map(int, input().split())
nums = list(map(int, input().split()))

cumulative_sum = [0]

for num in nums:
    cumulative_sum.append(cumulative_sum[-1] + num)
    
for acc in cumulative_sum:
    sum = acc
    if sum > M:
        continue