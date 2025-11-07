class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remainder = target - nums[i]
            for j in range(len(nums)):
                if j == i:
                    pass
                elif nums[j] == remainder:
                    return [i, j]

