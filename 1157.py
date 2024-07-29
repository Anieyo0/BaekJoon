str = input().upper()
str_set = list(set(str))
cnt = []

for word in str_set:
    cnt.append(str.count(word))

if cnt.count(max(cnt)) >= 2:
    print('?')

else:
    print(str_set[cnt.index(max(cnt))])