n = int(input())
a= []
result = []
min_diff = 1000000

for i in range(n):
    s, b = map(int,input().split())
    a.append([s,b])

def comb(cnt,sum1,sum2):
    global min_diff
    if cnt==n:
        if sum1!=1 and sum2!=0: 
            diff = abs(sum1-sum2)
            result.append(min(min_diff,diff))
        return
    for i in range(cnt, n):
        comb(i+1,sum1*a[cnt][0],sum2+a[cnt][1])
        comb(i+1,sum1,sum2)

comb(0,1,0)
print(min(result))