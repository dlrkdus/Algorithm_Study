from itertools import combinations

modi=list(input())
stk=[]
stack=[]
answer=set() #경우를 구하는 경우는 대부분 set을 쓰면 좋다(중복 배제)
comb=[]

for i in range(len(modi)):
    if modi[i]=="(":
        stk.append(i)
    elif modi[i]==")":
        stack.append((stk.pop(),i)) #modi에서 괄호의 인덱스


for i in range(len(stack)):
    for comb in list(combinations(stack, i+1)):
        arr=modi[:] #복사본
        for c in comb:
            arr[c[0]]=arr[c[1]]="" # 괄호쌍 지워주기
            #인덱스로 pop하면 안되나요?
            #안돼용. pop을 순서대로 할 때 arr에 변화가 생기기 때문.
        answer.add("".join(arr))

for i in sorted(answer):
    print(i)




            
