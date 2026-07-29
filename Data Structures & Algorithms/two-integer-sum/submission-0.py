class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index
    
        for x, y in enumerate(nums):
            difference = target - y
            if difference in prevMap:
                return [prevMap[difference], x]
            else:
                prevMap[y] = x