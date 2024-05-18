for test_case in range(1,11):
    N = int(input())
    pw = list(map(int,input().split()))
    K = int(input())
    cmd = list(input().split())

    i=0
    while(i<len(cmd)):  
        if cmd[i]=='I':
            list1 = pw[:int(cmd[i+1])]
            list2 = pw[int(cmd[i+1]):]
            
            list1+=cmd[i+3:i+3+int(cmd[i+2])]
            i+=(3+int(cmd[i+2]))
            pw = list1 + list2
        
        if i>=len(cmd):
            break

        if cmd[i]=='D':
            for j in range(int(cmd[i+2])):
                pw.pop(int(cmd[i+1]))
            i+=3

    print(f"#{test_case}", ' '.join(map(str,pw[:10])))