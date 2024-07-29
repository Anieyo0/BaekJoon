N = int(input())

user = []
for i in range(N):
    age, name = list(input().split())
    user.append([int(age), name, i])
    
sorted_user = sorted(user, key=lambda user: (user[0], user[2]))

for i in range(N):
    print(sorted_user[i][0], sorted_user[i][1])