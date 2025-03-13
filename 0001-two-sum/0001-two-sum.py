from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        # 딕셔너리를 먼저 초기화 시켜야 하는데, target으로 만들기 위한 
        for idx,num in enumerate(nums):
            # num이 target이 되기 위해 필요한 값이 dic에 있는지 
            if (target-num) in dic:
                return [idx, dic[target-num]]
            dic[num] = idx
        return []
