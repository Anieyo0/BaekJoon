def binary_search(P, page):
    l, r = 1, P
    c = int((l + r) / 2)
    cnt = 0
    
    while c != page:
        
        if c > page:
            r = c
            c = int((l + r) / 2)
            
        elif c < page:
            l = c
            c = int((l + r) / 2)
            
        cnt += 1
        
    return cnt


if __name__ == '__main__':
    TC = int(input())
    
    for i in range(TC):
        P, A, B = map(int, input().split())
        find_A_count = binary_search(P, A)
        find_B_count = binary_search(P, B)
        
        ans = 0 if find_A_count == find_B_count else 'A' if find_A_count < find_B_count else 'B'
        
        print(f'#{i+1} {ans}')