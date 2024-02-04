count=0
def solution(numbers, target):
    global count
    DFS(numbers, target, 0,0)
    return count

def DFS(numbers, target,level,s):
    global count
    if level==len(numbers):
        if s==target:
            count+=1
        return
    DFS(numbers, target, level+1, s + numbers[level])   
    DFS(numbers, target, level+1, s - numbers[level])
            
    