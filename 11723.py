import sys
input = sys.stdin.read

M = int(input())
S = 0

for _ in range(M):
    command = input().rstrip().split()
    
    if command[0] == 'all':
        S = (1 << 20) - 1
        
    elif command[0] == 'empty':
        S = 0
    
    elif command[0] == 'add':
        S |= (1 << int(command[1]))
        
    elif command[0] == 'remove':
        S &= ~(1 << int(command[1]))
        
    elif command[0] == 'toggle':
        S ^= (1 << int(command[1]))
        
    elif command[0] == 'check':
        if S & (1 << int(command[1])):
            print(1)
        else:
            print(0)