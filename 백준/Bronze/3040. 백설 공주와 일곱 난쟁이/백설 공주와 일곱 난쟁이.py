a = []
b=[0]*7
result = []
for i in range(9):
    n = int(input())
    a.append(n)

def comb(cnt, level, sum):
    if cnt == 7:
        if sum == 100:
            result.append(b.copy())  # b 리스트를 복사하여 result에 추가
        return 
    for i in range(level,9):
        b[cnt]=a[i]
        comb(cnt+1,i+1,sum+a[i])

comb(0,0,0)
for i in result[0]:
    print(i)