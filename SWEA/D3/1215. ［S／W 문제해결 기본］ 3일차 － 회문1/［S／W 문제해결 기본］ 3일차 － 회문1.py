for test_case in range(1,11):
    N = int(input())
    pan = [list(map(str,input())) for i in range(8)]
    pan2 = list(map(list,zip(*pan)))


    count=0

    for i in range(8):
        for j in range(0,8-N+1):
            arr = pan[i][j:j+N] #가로
            arr2 = pan2[i][j:j+N] #세로 
            arr_copy = arr.copy()
            arr2_copy = arr2.copy()
            arr.reverse()
            arr2.reverse()
            if arr_copy == arr:
                count+=1
            if arr2_copy == arr2:
                count+=1
                

    print(f"#{test_case}", count)
            

            
