N = int(input())

count = 0
for i in range(N):
    flag = True
    
    word = input()
    word_set = set(word)
    
    for index, alphabet in enumerate(word):
        if alphabet not in word_set:
            flag = False
            break
        
        if index == len(word) - 1:
            break
        
        next_alphabet = word[index + 1]
        if alphabet != next_alphabet:
            word_set.remove(alphabet)
        
    if flag:
        count += 1
        
print(count)
