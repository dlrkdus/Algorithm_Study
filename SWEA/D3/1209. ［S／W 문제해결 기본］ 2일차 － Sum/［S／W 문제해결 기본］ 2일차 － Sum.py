for test_case in range(1,11):
    tc = int(input())
    arr=[]
    result_a = [] #가로
    result_b = [0 for i in range(100)] #세로
    result_c = 0 # 우하
    result_d = 0 # 좌하
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        result_a.append(sum(arr[i])) #가로 
        for j in range(100): #세로
            result_b[j]+=arr[i][j]
        result_c+=arr[i][i]
        result_d+=arr[99-i][i]
        
    result = []
    result.append(max(result_a))
    result.append(max(result_b))
    result.append(result_c)
    result.append(result_d)


    print(f"#{test_case}",max(result))