import heapq
from collections import deque
def solution(book_time):
    count = 0
    room = []
    times = deque(convert(book_time))
    while times:
        time = times.popleft()
        if room and time[0] >= room[0]:
            heapq.heappop(room)
        else:
            count +=1
        heapq.heappush(room,time[1])
    return count

def convert(arr):
    tmp = []
    for a in arr:
        start = list(map(int,a[0].split(":")))
        end = list(map(int,a[1].split(":")))
        tmp.append([start[0]*60 + start[1], end[0]*60 + end[1] + 10])
    tmp.sort(key = lambda x:x[0])
    return tmp