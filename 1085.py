x, y, w, h = map(int, input().split())

distance = min(h-y, w-x, x, y)

print(distance)