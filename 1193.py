# X 입력받기
x = int(input())

# 짝수번째라인은 분자가 오름차순/분모가 내림차순
# 홀수번째라인은 분자가 내림차순/분모가 오름차순
line = 1

while x > line:
    x -= line
    line += 1
    
if line%2 == 0:
    a = x
    b = line-x+1
else:
    a = line-x+1
    b = x
print(a, '/', b, sep='')