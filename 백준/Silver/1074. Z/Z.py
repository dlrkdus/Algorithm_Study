
n,r,c=map(int,input().split())

def Z(n,r,c): 
    if n==0:
        return 0
    size = 2 ** (n-1)
    if r<size and c<size: #1사분면
        return Z(n-1,r,c)
    elif r>=size and c<size: #2사분면
        return 2**(2*(n-1))+Z(n-1,r-size,c)
    elif r<size and c>=size: #3사분면
        return 2**(2*(n-1))*2+Z(n-1,r,c-size)
    else: #4사분면
        return 2**(2*(n-1))*3+Z(n-1,r-size,c-size)
    

print(Z(n,c,r))
      