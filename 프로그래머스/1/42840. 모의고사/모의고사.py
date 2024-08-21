def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    sum = [0]*3
    
    for i in range(len(answers)):
        if answers[i]==s1[i%5]:
            sum[0]+=1
        if answers[i]==s2[i%8]:
            sum[1]+=1
        if answers[i]==s3[i%10]:
            sum[2]+=1
            
    max_sum = max(sum)   
    answer = []
    for i in range(3):
        if sum[i] ==max_sum:
            answer.append(i+1)
    return answer