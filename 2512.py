def binary_search(l, r):
    c = (l + r) // 2
    
    if l > r:
        return c
    
    budget = sum(map(lambda x: x if x < c else c, reqs))
    
    if budget == M:
        return c
    elif budget > M:
        return binary_search(1, c-1)
    
    else:
        return binary_search(c+1, r)
    

if __name__ == '__main__':
    N = int(input())
    reqs = list(map(int, input().split()))
    M = int(input())
    
    print(binary_search(0, max(reqs)))