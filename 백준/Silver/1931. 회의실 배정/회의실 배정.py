n = int(input())
meeting = []
for _ in range(n):
    arr = list(map(int, input().split()))
    meeting.append(arr)
meeting.sort(key=lambda x: (x[1],x[0])) #빨리 끝나는 회의순으로 정렬
#빨리 시작하는 순으로 정렬하면 언제 끝날지 모르니 뒤를 고려하기 애매해진다.

result=[]
time=0
for i in range(n):
    if meeting[i][0]>=time:
        result.append(meeting[i])
        time=meeting[i][1]
print(len(result))

    

