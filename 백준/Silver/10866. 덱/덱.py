import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front": #덱의 맨 앞 삽입
        d.appendleft(cmd[1]) #appendleft()
    elif cmd[0] == "push_back": #덱의 맨 뒤 삽입
        d.append(cmd[1]) #append

    elif cmd[0] == "pop_front": #가장 앞 수 빼기
        if len(d) != 0: print(d.popleft()) #popleft()
        else: print(-1)
    elif cmd[0] == "pop_back": #가장 뒤 수 빼기
        if len(d) != 0: print(d.pop()) #pop()
        else: print(-1)

    elif cmd[0] == "size":
        print(len(d))

    elif cmd[0] == "empty":
        if len(d) == 0: print(1)
        else : print(0)

    elif cmd[0] == "back":
        if len(d) == 0: print(-1)
        else: print(d[len(d) -1])

    elif cmd[0] == "front":
        if len(d) == 0: print(-1)
        else: print(d[0])