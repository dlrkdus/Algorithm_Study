def solution(s):
    answer = len(s)
    for unit in range(1, len(s)//2 + 1):
        count = 1
        comp = ''
        repeat = s[:unit]
        for i in range(unit, len(s), unit):
            # 반복된다면 개수 누적
            if s[i:i+unit] == repeat:
                count +=1
            # 반복이 끊겼다면
            else:
                # 압축하기
                if count >=2:
                    comp += str(count)+repeat
                else:
                    comp += repeat
                # 새로운 반복 문자열 갱신 및 개수 초기화
                repeat = s[i:i+unit]
                count = 1
        # 마지막 반복 문자열은 압축이 안됐으므로 직접 해줌
        if count >= 2:
            comp +=str(count) + repeat
        else:
            comp += repeat
        
        answer = min(answer,len(comp))
    return answer
        
        
        
