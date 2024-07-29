n = int(input())

def find_end_num(n):
    count = 0
    end_num = 0
    num = 666
    while True:
        if count == n:
            return print(end_num)
        
        if '666' in str(num):
            end_num = num
            count += 1
        num += 1
        
    
    
find_end_num(n)