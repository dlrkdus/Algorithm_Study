arr = list(input())
x,y = 0,0
tmp = []
while y<len(arr):
    if arr[y]=="-" or arr[y]=="+":
        tmp.append(int(''.join(map(str,arr[x:y]))))
        tmp.append(arr[y])
        x = y + 1
    y+=1
    if y == len(arr):
        tmp.append(int(''.join(map(str,arr[x:]))))

dp_min = [[float('inf') for i in range(50)]for j in range(50)]
dp_max = [[float('-inf') for i in range(50)]for j in range(50)]

# 숫자는 초기화
for i in range(0,len(tmp),2):
    dp_min[i][i] = tmp[i]
    dp_max[i][i] = tmp[i]

# 무조건 2개씩 건너뛰기 
for length in range(1,len(tmp)+1,2):
    for start in range(0,len(tmp)-length+1,2):
        end = start +length-1
        for i in range(start+1,end,2):
            if tmp[i] == "+":
                dp_min[start][end] = min(dp_min[start][end],dp_min[start][i-1] + dp_min[i+1][end])
                dp_max[start][end] = max(dp_max[start][end],dp_max[start][i-1] + dp_max[i+1][end])
            if tmp[i] == "-":
                dp_min[start][end] = min(dp_min[start][end],dp_min[start][i-1] - dp_max[i+1][end])
                dp_max[start][end] = max(dp_max[start][end],dp_max[start][i-1] - dp_min[i+1][end])
print(dp_min[0][len(tmp)-1])

