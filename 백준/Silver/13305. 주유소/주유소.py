N = int(input())
km = list(map(int,input().split()))
oil = list(map(int,input().split()))
oil.pop()
min = oil[0]
restKm = sum(km)
result=0

for i in range(len(km)):
    if oil[i]<min:
        min=oil[i]
    result+=km[i]*min
print(result)
