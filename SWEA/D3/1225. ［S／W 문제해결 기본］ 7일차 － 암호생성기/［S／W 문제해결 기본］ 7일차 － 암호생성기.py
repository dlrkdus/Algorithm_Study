
for test_case in range(1,11):
    tc = int(input())
    d = list(map(int,input().split()))
    i=1
    while(d[len(d)-1]>0):
        d.append(d.pop(0)-i)
        if d[len(d)-1]<0:
            d[len(d)-1]=0
        if i<5:
            i+=1
        else:
            i=1
    print(f"#{test_case}",' '.join(map(str,d)))


