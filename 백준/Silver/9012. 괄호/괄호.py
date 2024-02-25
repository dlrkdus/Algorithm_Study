n=int(input())
for i in range(n):
    arr=[]
    my_str=str(input())
    for x in my_str:
        if x=="(":
            arr.append(x)
        else:
            if len(arr)==0:
                print("NO")
                break
            else:
                arr.pop()
    else:
        if len(arr)==0:
            print("YES")
        else:
            print("NO")
       
