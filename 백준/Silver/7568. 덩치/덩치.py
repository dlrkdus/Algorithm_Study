N = int(input())
people = []
for i in range(N):
    x, y = map(int,input().split())
    people.append([x,y])


for i in people: # 랭크 매길 사람람
    rank = 1
    for j in people: # 비교용 반복문
        if i[0] < j[0] and i[1] < j[1]: # 키와 몸무게 둘 다 작다면면
            rank +=1 # 랭크 낮추기
    print(rank, end = ' ')

