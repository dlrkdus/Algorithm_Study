n,m=map(int,input().split())
a=set()
for i in range(n):
    a.add(input())
b=set()
for i in range(m):
    b.add(input())
result=sorted(list(a&b))#파이썬의 교집합 연산자 &
print(len(result))
for i in result:
    print(i)