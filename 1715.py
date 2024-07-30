import sys
input = sys.stdin.readline

from heapq import heappop, heappush, heapify

N = int(input())
# cards = [int(input()) for _ in range(N)]
# heapify(cards)
# heapify는 시간이 조금 더 오래걸림
cards = []
for _ in range(N):
    heappush(cards, int(input()))

cnt = 0
while len(cards) > 1:
    A, B = heappop(cards), heappop(cards)
    cnt += A + B
    heappush(cards, A + B)
    
print(cnt)