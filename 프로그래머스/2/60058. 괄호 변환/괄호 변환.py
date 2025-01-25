# solution의 역할은 균형 잡힌 문자열을 올바른 문자열로 바꾸어주는 역할이다.
# 균형 잡혀있으므로 (와 )를 적절히 뒤집기만 하면 올바른 문자열이 된다.
def solution(p):
    if not p:
        return ''
    u, v = seperate(p)
    if isCorrect(u):
        return u + solution(v)
    else:
        # 첫번째와 마지막을 (와 )로 맞추는 이유는, )로 시작될 수 없기 때문이다.
        answer = '('
        answer += solution(v)
        answer += ')'
        for s in u[1:len(u)-1]:
            if s =='(':
                answer +=')'
            else:
                answer +='('
        return answer
                
    

def seperate(p):
    a = 0
    b = 0
    for i in range(len(p)):
        if p[i] == '(':
            a+=1
        else:
            b+=1
        if a==b:
            return p[:i+1], p[i+1:]

def isCorrect(arr):
    stack = []
    for a in arr:
        if a =='(':
            stack.append(a)
        else:
            if not stack:
                return False
            stack.pop()
                
    if not stack:
        return True
    return False