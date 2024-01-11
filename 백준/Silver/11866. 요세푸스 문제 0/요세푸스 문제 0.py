n,k=map(int,input().split())
queue=[i for i in range(1, n+1)]
arr=[]
index=0
while queue:
    index+=(k-1)
    if index>=len(queue):
        index=index%len(queue)
    arr.append(str(queue.pop(index))) 

output = '<' + ', '.join(arr) + '>'
print(output)