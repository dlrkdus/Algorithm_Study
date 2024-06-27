from collections import deque
import sys
left = deque(sys.stdin.readline().strip())
right = deque()
M = int(sys.stdin.readline().strip())



for _ in range(M):
    command = list(sys.stdin.readline().strip())
    c_index = len(left) #커서 위치 
    if command[0] =='L' and left: #left 가 비어있지 않다면 
        right.appendleft(left.pop())
    if command[0] =='D' and right: #right 가 비어있지 않다면 
        left.append(right.popleft())
    if command[0] == 'B' and left:
        left.pop()
    if command[0] == 'P':
        left.append(command[2])

print(''.join(left) + ''.join(right))

    