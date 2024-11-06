from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
        
    return bfs(begin, target, words)

def bfs(begin, target, words):
    q = deque()
    q.append([begin,0]) # 초기 단어와 단계를 큐에 넣어준다. 
    while q:
        now, step = q.popleft() # 현재 단어와 단계를 뽑는다. 
        if now == target:
            return step
        for word in words:
            count = 0
            for i in range(len(word)):
                if word[i]==now[i]:
                    count+=1
            if count == len(word)-1: # 한 번에 한 개의 알파벳만 바꿀 수 있으므로 
                q.append([word,step+1])
