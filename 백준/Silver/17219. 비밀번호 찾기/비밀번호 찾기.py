n,m=map(int,input().split())
find_pw={} #딕셔너리로 푼다.

for i in range(n):
    site,pw=input().split()
    find_pw[site]=pw

for i in range(m):
    find=input()
    print(find_pw[find])