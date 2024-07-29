def fibo(n):
    if n <= 1:
        return n
    
    return fibo(n-2) + fibo(n-1)
    
if __name__ == '__main__':
    n = int(input())
    print(fibo(n))