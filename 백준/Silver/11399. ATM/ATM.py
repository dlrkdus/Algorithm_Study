n = int(input()) 
arr = list(map(int, input().split()))  
answer = 0  

arr.sort()

for x in range(1, n+1):
    answer += sum(arr[0:x])  
print(answer)  