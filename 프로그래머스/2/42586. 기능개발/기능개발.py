def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0:          
            progresses[i]=(100-progresses[i])/speeds[i]
        else:
            progresses[i]=(100-progresses[i])//speeds[i]+1
    i=0
    while i<len(progresses):
        max=progresses[i]
        i+=1
        sum=1
        while i<len(progresses) and progresses[i]<=max:
            sum+=1
            i+=1
        answer.append(sum)

                
    return answer