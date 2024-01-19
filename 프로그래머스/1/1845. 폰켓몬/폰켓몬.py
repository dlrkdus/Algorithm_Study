def solution(nums):
    arr={}
    sum=0
    for i in nums:
        arr[i]=arr.get(i,0)+1
    species=sorted(arr.items(),key=lambda x:x[1]) #종류별 수량으로 오름차순 정렬
    if len(species)<=len(nums)/2: #종류 수가 최대로 가져갈 수 있는 수량보다 적으면
        return len(species) 
    else: #종류 수가 최대로 가져갈 수 있는 수량보다 많으면
        return int(len(nums)/2) 