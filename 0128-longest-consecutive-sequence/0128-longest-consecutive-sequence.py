class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = sorted(set(nums))
        if len(n) == 0 :
            return 0
        count = 1
        for i in range(1,len(n)):
            if n[i] != n[i-1] + 1:
                break
            count += 1
        return count