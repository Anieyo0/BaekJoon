from itertools import permutations

TC = int(input())

for _ in range(TC):
    
    CANNOT_MAKE_PALINDROME_FLAG = True
    WORD_NUM = int(input())
    
    words = []
    for _ in range(WORD_NUM):
        words.append(input())
        
    palindrome_word = list(map(''.join, permutations(words, 2)))
     
    for word in palindrome_word:
        if word == word[::-1]:
            CANNOT_MAKE_PALINDROME_FLAG = False    # 회문 가능한 문자
            print(word)
            break
      
    if CANNOT_MAKE_PALINDROME_FLAG:
        print('0')