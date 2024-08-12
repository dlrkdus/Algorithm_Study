
n = int(input())
row = [0 for i in range(n)] # 각 요소는 퀸의 행 위치 
# arr[i] = j 는 [i,j]와 같다 

def attackable(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return True
    return False


def nQueen(start):
    global count
    if start == n:
        count+=1
        return
    for i in range(n):
        row[start]= i 
        if not attackable(start):
            nQueen(start+1)


    
count = 0
nQueen(0)
print(count)
