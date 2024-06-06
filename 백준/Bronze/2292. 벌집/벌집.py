N = int(input())
# 6, 12, 18, 24, ..
# 2~7까진 1, 8~19까진 2,  20~37까진 3, 38~61까진 4,, 
i=1
result = 1
n=1
while N>n:
    n+=6*i
    i+=1
    result+=1
print(result)