def solution(nums):
    arr={}
    for i in nums:
        arr[i]=arr.get(i,0)+1
    species=sorted(arr.items(),key=lambda x:x[1]) #종류 수로 정렬,튜플
    return min(len(species),len(nums)/2)