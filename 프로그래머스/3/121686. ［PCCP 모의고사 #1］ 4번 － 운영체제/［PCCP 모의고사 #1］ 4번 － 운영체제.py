import heapq
from collections import deque
def solution(program):
    # 점수, 호출 시각, 실행 시간
    # 점수가 낮을수록 우선순위가 높다. 우선순위 순으로 실행된다.
    # 우선순위가 낮더라도 실행중이라면 이를 중단시키진 않는다.
    # 즉, 호출 시각 -> 점수 우선 순으로 실행된다.
    answer = [0] * 11
    wait = [] # 대기열, 호출 시각을 1순위, 점수를 2순위로 정렬
    program.sort(key = lambda x: (x[1],x[0])) # 프로그램 우선순위 정렬
    time = 0 # 현재 시각
    total = 0
    while program or wait: # 프로그램과 대기열이 남아있지 않을 때까지
        # 우리는 대기열을 처리할 거다 !
        while program and not wait: # 대기열이 없다면 
            time = program[0][1] # 시간 땡겨주기
            heapq.heappush(wait,program.pop(0))
        if wait: # 대기열이 있다면 처리한다.
            current = heapq.heappop(wait)
            answer[current[0]] += time - current[1]
            time += current[2]
        while program and program[0][1] <= time: # 프로그램이 남아있다면 대기열 리필해준다.
            heapq.heappush(wait,program.pop(0))
    answer[0] = time
    return answer
    