from itertools import combinations

n, m = map(int, input().split())
card_list = list(map(int, input().split()))

sum = [sum(i) for i in combinations(card_list, 3) if sum(i) <= m]

print(max(sum))