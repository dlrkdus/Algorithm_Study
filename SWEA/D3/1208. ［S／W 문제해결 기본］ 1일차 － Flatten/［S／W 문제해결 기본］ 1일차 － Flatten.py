for test_case in range(1,11):
    dump = int(input())
    box = list(map(int,input().split()))

    while(dump>0):
        max_index = box.index(max(box))
        min_index = box.index(min(box))
  
        box[max_index]-=1
        box[min_index]+=1
        dump-=1
    
    print(f"#{test_case}", max(box)-min(box))