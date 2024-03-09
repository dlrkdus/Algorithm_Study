n,m=map(int,input().split())
S=[input() for _ in range(n)]
A=(input() for _ in range(m))

count=0

for i in A:
    if i in S:
        count+=1
print(count)