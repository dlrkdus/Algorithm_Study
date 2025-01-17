N = input()
arr = list(map(int,N))
left = arr[:(len(arr)//2)]
right = arr[(len(arr)//2):]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")