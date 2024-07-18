N = int(input())
A = list(map(int,input().split()))
calc = list(map(int,input().split()))
sumArr = []
maxNum = -float('inf')
minNum = float('inf')

def backtrack (level,result):
    global maxNum,minNum
    if level == len(A):
        maxNum = max(maxNum, result)
        minNum = min(minNum, result)
        return 
    for j in range(4):
        if calc[j]>0:
            calc[j]-=1
            if j == 0:
                backtrack(level+1, result+A[level])
            if j == 1:
                backtrack(level+1, result-A[level])
            if j == 2:
                backtrack(level+1, result*A[level])
            if j == 3:
                if result < 0:
                    backtrack(level+1, -(-result//A[level]))
                else:
                    backtrack(level+1, result//A[level])
            calc[j]+=1
            
backtrack(1, A[0])
            
print(maxNum)
print(minNum)
                