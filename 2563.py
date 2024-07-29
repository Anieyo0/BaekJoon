PAPER_LENGTH = 10
N = int(input())

paper = [[0] * 100 for _ in range(100)]

for _ in range(N):  # 색종이 좌표 입력 블록
    xy = list(map(int, input().split()))    # 색종이 좌표 (2차원 리스트)
    
    for i in range(xy[0], xy[0] + 10):
        for j in range(xy[1], xy[1] + 10):
            paper[i][j] = 1
            
print(sum(row.count(1) for row in paper)) 
