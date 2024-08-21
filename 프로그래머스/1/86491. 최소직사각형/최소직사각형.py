def solution(sizes):
    height = 0
    weight = 0

    for s in sizes:
        #정렬해주기
        if s[0]<s[1]:
            s[0],s[1] = s[1],s[0]
        weight = max(weight,s[0])
        height = max(height,s[1])
            
        print(weight, height)
            
            
    return weight*height