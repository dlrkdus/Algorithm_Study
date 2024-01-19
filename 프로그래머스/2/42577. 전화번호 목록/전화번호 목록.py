def solution(phone_book):
    answer = True
    pb=sorted(phone_book)
    for i in range(len(pb)-1):
        if pb[i+1].startswith(pb[i]): #접두사 확인
            answer=False
            break
    return answer