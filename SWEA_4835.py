TC = int(input())

for tc in range(TC):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    cumulative_sum = [0]
    
    for num in nums:
        cumulative_sum.append(cumulative_sum[-1] + num)
        
    max_sum = 0
    min_sum = float('inf')
    
    for i in range(N-M+1):
        sum = cumulative_sum[i+M] - cumulative_sum[i]
        
        max_sum = max(max_sum, sum)
        min_sum = min(min_sum, sum)
           
    print(f'#{tc+1} {max_sum - min_sum}')
            