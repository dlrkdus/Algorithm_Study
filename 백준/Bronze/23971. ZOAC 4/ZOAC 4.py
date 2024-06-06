H, W, N, M = map(int,input().split())

if (H%(N+1))!=0:
    h = (H//(N+1))+1
else:
    h = (H//(N+1))

if (W % (M+1))!=0:
    w = (W // (M+1))+1
else:
    w = (W // (M+1))

answer = h*w

print(answer)