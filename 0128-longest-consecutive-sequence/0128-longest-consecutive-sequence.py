class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = sorted(set(nums))
        if len(n) == 0 :
            return 0
        print(n)
        count = 1
        arr = []
        for i in range(len(n)):
            if i == len(n)-1 or n[i]+1 != n[i+1]:
                arr.append(count)
                print(count)
                count = 0
            count += 1
        return max(arr)