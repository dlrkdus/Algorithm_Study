import heapq
from collections import deque
def solution(book_time):
    book = deque(convert(book_time))
    now = 0
    room = []
    while book:
        now_book = book.popleft()
        if room and room[0]<=now_book[0]:
            heapq.heappop(room)
        heapq.heappush(room,now_book[1])
    return len(room)
        

def convert(arr):
    tmp = []
    for a in arr:
        start = list(map(int,a[0].split(":")))
        end = list(map(int,a[1].split(":")))
        tmp.append([start[0]*60 + start[1], end[0]*60 + end[1] + 10])
    tmp.sort(key = lambda x:x[0])
    return tmp