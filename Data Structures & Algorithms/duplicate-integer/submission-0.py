class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #i can only think of the brute force
        # run thru once compare x to another run of every x, if match return true
        # if not return false
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False