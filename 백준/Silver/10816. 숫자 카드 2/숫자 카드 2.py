n = int(input())
card = input().split()

card_count = {}
for c in card:
    card_count[c] = card_count.get(c, 0) + 1
    #딕셔너리의 get(찾고자 하는 key, key값이 없을시 반환할 기본값)
    #card_count[c]에 값이 있으면(전에 나왔으면) 값을 가져오고,
    #없으면 0을 저장한다.
    #모두 +1을 해준다.
   
m = int(input())
find_card = input().split()

result = [card_count.get(c, 0) for c in find_card]
print(*result)