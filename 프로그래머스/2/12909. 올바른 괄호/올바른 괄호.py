def solution(s):
    answer = True
    arr=[]
    
    for parent in s:
        if parent=="(":
            arr.append(parent)
        if parent==")":
            if len(arr)==0:
                answer=False
                break
            else:
                arr.pop()
    if len(arr)>0:
        answer=False

    return answer
        
            
    