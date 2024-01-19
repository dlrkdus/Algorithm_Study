from collections import Counter
def solution(participant, completion):
    
    participant=Counter(participant)
    completion=Counter(completion)
    answer = list(participant-completion)
    return answer[0]