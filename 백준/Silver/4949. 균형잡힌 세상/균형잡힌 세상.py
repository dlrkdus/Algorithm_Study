while(True):
    a=input()
    stack=[]
    if a=='.':
        break
    else:
        f=0
        for i in a:
            if i=='(' or i=='[':
                stack.append(i)
            if i==')':
                if len(stack)>0 and stack.pop()=='(':
                    continue
                else:
                    f=1
                    break
                    
            if i==']':
                if len(stack)>0 and stack.pop()=='[':
                    continue
                else:
                    f=1
                    break
                    
        if len(stack)==0 and f==0:
            print("yes")
        else:
            print("no")
                
