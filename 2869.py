a, b, height = map(int, input().split())

days = (height - a) / (a - b) + 1
if days != int(days):
    days = int(days) + 1

print(int(days))