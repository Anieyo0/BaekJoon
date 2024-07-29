angle = []
for _ in range(3):
    angle.append(int(input()))

if sum(angle) != 180:
    print('Error')
elif sum(angle) == 180 and len(set(angle)) == 2:
    print('Isosceles')
elif sum(angle) == 180 and len(set(angle)) == 3:
    print('Scalene')
elif angle.count(60):
    print('Equilateral')