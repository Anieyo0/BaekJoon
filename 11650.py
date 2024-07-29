N = int(input())

xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))
   
xy.sort() 
    
for i in range(N):
    print(xy[i][0], xy[i][1])