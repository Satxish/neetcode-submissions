class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count  = res = 0
        for x in nums:
            if x == 0:
                res = max(count,res)
                count = 0
            else:
                count += 1
        return max(count,res)
        