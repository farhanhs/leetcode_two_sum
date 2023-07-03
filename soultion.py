class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            if target == nums[i]+nums[i-1]:
                output = [i-1,i]
        return output
