from statistics import median

k, n = map(int, input().split())
string = [int(input()) for i in range(k)]
start=1
end=max(string)

while (start<=end):
    mid=(start+end)//2
    s=sum(element // mid for element in string) # 선 개수

    if s>=n:
        start=mid+1
    elif s<n:
        end=mid-1

print(end)



    
