TC = int(input())

quiz_result = []
for _ in range(TC):
    quiz_result.append(input())

for i in range(TC):
    score = 0
    temp = 0    # 자릿수마다의 점수 계산을 위한 변수
    for j in range(len(quiz_result[i])):
        if quiz_result[i][j] == 'O':
            temp += 1
            score += temp
        
        else:   # 'X'일 경우
            temp = 0
            
    print(score)    # 점수 출력 후 변수 초기화
