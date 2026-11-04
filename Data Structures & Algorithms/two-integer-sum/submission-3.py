class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i,n in enumerate(nums):
            Map[n] = i
        for i ,n in enumerate(nums):
            diff = target - n
            if diff in Map and Map[diff] != i:
                return [i, Map[diff]]
            Map[n] = i

        