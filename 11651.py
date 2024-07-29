N = int(input())

xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))
   
sorted_xy = sorted(xy, key=lambda xy: (xy[1], xy[0]))
    
for i in range(N):
    print(sorted_xy[i][0], sorted_xy[i][1])