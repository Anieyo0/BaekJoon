lengths = list(map(int, input().split()))

is_valid = True
if max(lengths) >= sum(lengths) - max(lengths):
    is_valid = False
    
if is_valid:
    print(sum(lengths))
    
else:
    longest_side = sum(lengths) - max(lengths) - 1
    print(sum(lengths) - max(lengths) + longest_side)