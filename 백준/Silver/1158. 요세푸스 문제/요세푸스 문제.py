
n,k=map(int,input().split())
q=[i for i in range(1,n+1)]
arr=[]
i=0

while q:
    i+=(k-1)
    if i>=len(q):
        i=i%len(q)   
    arr.append(q.pop(i))

output = '<' + ', '.join(map(str, arr)) + '>'

print(output)
