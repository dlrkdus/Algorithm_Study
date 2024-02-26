n=int(input())
ballons=list(map(int,input().split()))
idx=0 #0번째부터 시작
index=[x for x in range(1,n+1)]
answer=[]
temp = ballons.pop(idx)
answer.append(index.pop(idx))

while ballons:
    if temp<0: #음수라면
        idx = (idx+temp)%len(ballons)
    else:
        idx=(idx+temp-1)%len(ballons)
    temp = ballons.pop(idx)
    answer.append(index.pop(idx))

for i in answer:
    print(i,end=' ')
