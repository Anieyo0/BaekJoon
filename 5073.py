while True:
    is_valid = True
    
    lengths = list(map(int, input().split()))
        
    if lengths.count(0) == 3:
        break
    
    if max(lengths) >= sum(lengths) - max(lengths):
        is_valid = False
        
    if len(set(lengths)) == 1 and is_valid:
        print('Equilateral')
        
    elif len(set(lengths)) == 2 and is_valid:
        print('Isosceles')
        
    elif len(set(lengths)) == 3 and is_valid:
        print('Scalene')
        
    else:
        print('Invalid')
