class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) ==2 & nums[0]+nums[1] == target:
            return [0,1]
        for i in range(len(nums)):
            required = target- nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] ==required:
                    return [i,j]

        