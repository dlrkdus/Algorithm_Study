N = int(input())
km = list(map(int,input().split()))
oil = list(map(int,input().split()))
oil.pop()
min = min(oil)
restKm = sum(km)
result=0

for i in range(len(km)):
    if oil[i]==min:
        result += restKm*oil[i]
        break
    else:
        restKm-=km[i]
        result+=km[i]*oil[i]

print(result)
