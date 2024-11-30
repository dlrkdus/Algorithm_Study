def solution(storey):
    answer = 0
    
    while storey > 0:
        current_digit = storey % 10  # 현재 자리수
        next_digit = (storey // 10) % 10  # 다음 자리수
        
        # 현재 자리수를 기준으로 올림 또는 내림 결정
        if current_digit > 5 or (current_digit == 5 and next_digit >= 5):
            answer += 10 - current_digit  # 올림
            storey += 10  # 다음 자리로 올림
        else:
            answer += current_digit  # 내림
            
        storey //= 10  # 다음 자리로 이동
    
    return answer