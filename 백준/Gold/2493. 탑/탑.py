n=int(input())
tower=list(map(int,input().split()))

answer=[]
stack=[]
for i in range(n):
    while stack:
        if stack[-1][0]>tower[i]:
            answer.append(stack[-1][1]+1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([tower[i],i])

    
print(' '.join(map(str,answer)))
        
