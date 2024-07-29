import sys

N = int(sys.stdin.readline().rstrip())

attendance = dict()
for _ in range(N):
    name, state = sys.stdin.readline().rstrip().split()
    attendance[name] = state
 
people_in_company = [name for name, state in attendance.items() if state == 'enter']
    
people_in_company.sort(reverse=True)    # 사전 역순으로 정렬
for person in people_in_company:
    print(person)