n,k=map(int,input().split())
arr=list(map(int,input().split()))
start=1
end=max(arr)

while start<=end:   
    h=(start+end)//2
    tree_sum = sum(x - h for x in arr if x > h)
    if tree_sum>=k: #h가 너무 낮다
        start=h+1
    elif tree_sum<k: #h가 너무 높다
        end=h-1

print(end)
