import heapq
N=int(input())
heap=[]
for i in range(N):
    nums= map(int,input().split()) # 한 줄 입력
    for n in nums:
        if len(heap)<N:
            heapq.heappush(heap,n)
        else:
            if heap[0]<n:
                heapq.heappop(heap)
                heapq.heappush(heap,n)
print(heapq.heappop(heap))


# N 크기의 heap을 사용하자. 
# heap이 꽉 차있을 때 최소값보다 작은 값이 들어오면 무시하면 된다. 
# 즉 heap에는 배열에서 1~n번째 큰 수가 저장되는거다.
# 반환할 때는 heap의 최소값을 반환하면 된다. (n 크기의 힙에서 n번째 큰 수니)

