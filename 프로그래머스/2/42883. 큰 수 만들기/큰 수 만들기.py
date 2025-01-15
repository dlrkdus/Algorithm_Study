def solution(number, k):
    # 스택을 활용하는 문제
    stack = []
    for n in number:
        while len(stack)>0 and stack[-1] < n and k>0:
            stack.pop()
            k-=1
        stack.append(n)
    if k!=0:
        return ''.join(map(str,stack[:len(number)-k]))
    return ''.join(map(str,stack))
    
# 반례 : number가 내림차순일 때(54321) stack은 54321이 된다.