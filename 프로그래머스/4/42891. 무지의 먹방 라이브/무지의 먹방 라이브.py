import heapq 
def solution(food_times, k):
    if sum(food_times) <= k : 
        return -1
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq,(food_times[i],i+1))
    
    sum_eat = 0 # 먹기 위해 사용한 시간
    priv_eat = 0 # 직전에 다 먹은 음식 시간
    left_food = len(food_times) # 남은 음식 개수
    
    # 먹기 위해 사용한 시간 + (현재 음식 시간 - 이전 음식 시간)* 남은 음식 개수 가 K를 넘으면 안됨
    while sum_eat + ((hq[0][0]-priv_eat)*left_food) <= k:
        now = heapq.heappop(hq)[0]
        sum_eat +=(now-priv_eat) * left_food
        left_food -=1
        priv_eat = now
        
    result = sorted(hq,key = lambda x:x[1]) # 음식 번호 기준으로 정렬
    return result[(k-sum_eat)%left_food][1]
            
        
            