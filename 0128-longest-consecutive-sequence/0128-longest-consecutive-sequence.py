class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_dict = {}
        # 해시에 넣는 이유는 배열에서 요소를 찾는 것보다 해시에서 키를 찾는게 더 빠르기 떄문이다
        for num in nums:
            num_dict[num] = True # value는 의미 없다.
        for num in num_dict: # 당연히 for문의 in과 배열에 있는지 확인하는 in은 다르다.
            if num - 1 not in num_dict: # num이 수열의 최소값이라면 
                count = 1
                target = num + 1 # 증가하기 위해서 다음에 있어야 하는 값
                while target in num_dict:
                    target +=1
                    count +=1
                longest = max(longest,count)
        return longest