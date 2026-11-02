class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final = set()
        for num in nums:
            if num in final:
                return True
            final.add(num)
        return False

        