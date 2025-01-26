N = int(input())
numbers = list(map(int,input().split()))
o = list(map(int,input().split()))
min_num = 10000000000000
max_num = -1000000000000

def dfs(level,result):
    global min_num,max_num
    if level == N:
        min_num = min(min_num,result)
        max_num = max(max_num,result)
        return
    for i in range(4):
        if o[i] > 0:
            o[i]-=1
            if i == 0:
                dfs(level+1,result+numbers[level])
            if i == 1:
                dfs(level+1,result-numbers[level])
            if i == 2:
                dfs(level+1,result*numbers[level])
            if i ==3:
                if result < 0:
                    dfs(level+1,-(-result//numbers[level]))
                else:
                    dfs(level+1,result//numbers[level])
            o[i]+=1

dfs(1,numbers[0])

print(max_num)
print(min_num)
