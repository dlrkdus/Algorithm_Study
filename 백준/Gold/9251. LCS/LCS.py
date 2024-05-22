import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
m=len(word1)
n=len(word2)
arr = [[0] * (n+1) for _ in range(m+1)] #이차원 배열,
#0으로 초기화
ans=0

def LCS(m,n):
    if m==0 or n==0:
        return 0
    else:
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    arr[i][j]=arr[i-1][j-1]+1
                else:
                    arr[i][j]=max(arr[i][j-1],arr[i-1][j])
    return arr[m][n]

print(LCS(m,n))
