import sys
from itertools import combinations

heights = []
for _ in range(9):
    heights.append(int(sys.stdin.readline().strip()))
    
for c in combinations(heights, 7):
    if sum(c) == 100:
        heights = sorted(c)
        
        for height in heights:
            print(height)
        break