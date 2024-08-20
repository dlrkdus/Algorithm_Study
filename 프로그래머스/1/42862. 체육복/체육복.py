def solution(n, lost, reserve):
    reserve_only = sorted(list(set(reserve) - set(lost)))
    lost_only = sorted(list(set(lost) - set(reserve)))
    answer = 0
    
    for l in lost_only:
        if l - 1 in reserve_only:
            reserve_only.remove(l - 1)
            answer += 1
        elif l + 1 in reserve_only:
            reserve_only.remove(l + 1)
            answer += 1
            
    print(answer)
    answer = n-(len(lost_only)-answer)
    return answer