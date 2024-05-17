T = int(input())

for test_case in range(1,T+1):
    tc, l = input().split()
    l = int(l)
    str_arr = ["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]
    int_arr = [0,1,2,3,4,5,6,7,8,9]
    num = list(map(str,input().split()))
    dic = {}
    arr= []

    for i in num:
        arr.append(int_arr[str_arr.index(i)])
    
    arr.sort()
    result = []

    for n in arr:
        result.append(str_arr[n])
    
    print(f"#{test_case}")
    print(' '.join(map(str,result)))