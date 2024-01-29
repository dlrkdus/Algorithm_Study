import heapq
def solution(heap, K):
    #알고리즘: 가장 작은 값이 k 이상일 때까지 정렬하며 mix 해준다. mix는 최소값끼리 해준다.
    #하지만 1,000,000이라는 scoville의 길이상 매번 정렬을 하면 시간초과가 난다.
    #이때 루트가 항상 최소값인 힙을 사용하면 효율적인 시간을 낼 수 있다.
    count=0
    heapq.heapify(heap) #리스트 heapify
    
    while heap[0]<K: #최소값이 k 이상일 때까지 반복하겠다.
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        count+=1
        if len(heap) == 1 and heap[0] < K: #마지막 남은 요소조차 k보다 크다면 만들 수 없는것
            return -1
    return count
        
        
    
    