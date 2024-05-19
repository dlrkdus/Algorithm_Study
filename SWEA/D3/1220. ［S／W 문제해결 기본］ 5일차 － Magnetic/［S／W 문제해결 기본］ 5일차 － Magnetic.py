for test_case in range(1,11):
    T = int(input())
    table = [list(map(int, input().split()))for i in range(100)]
    table2 = list(map(list,zip(*table)))
    count=0

    # 1 = N / 2 = S
    for arr in table2:
        if sum(arr)==1 or sum(arr)==2:
            continue
        arr = [x for x in arr if x != 0]
        arr_str = ''.join(map(str,arr))
        count+=arr_str.count("12")

    print(f"#{test_case}", count)



