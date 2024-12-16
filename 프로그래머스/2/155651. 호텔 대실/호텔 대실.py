import heapq
from collections import deque
def solution(book_time):
    count = 0
    time = convert(book_time)
    hotel = []
    for t in time:
        if len(hotel) == 0:
            heapq.heappush(hotel,t[1])
        else:
            if hotel[0] <= t[0]:
                heapq.heappop(hotel)
            heapq.heappush(hotel,t[1])
    return len(hotel)

def convert(arr):
    tmp = []
    for a in arr:
        start = list(map(int,a[0].split(":")))
        end = list(map(int,a[1].split(":")))
        tmp.append([start[0]*60 + start[1], end[0]*60 + end[1] + 10])
    tmp.sort(key = lambda x:x[0])
    return tmp