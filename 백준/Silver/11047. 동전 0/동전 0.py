N, K = map(int,input().split())

c=[]
result = 0

for i in range(N):
    coin = int(input())
    c.append(coin)

for i in reversed(range(N)):
    result+= (K//c[i])
    K%=c[i]

print(result)