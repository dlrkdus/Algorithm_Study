import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = {}
count = 0

for _ in range(N):
  S[input()] = 0

for _ in range(M):
  if input() in S:
    count += 1

print(count) 
