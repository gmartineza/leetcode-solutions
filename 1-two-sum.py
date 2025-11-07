"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            for j in range(len(nums)):
                if j == i:
                    pass
                elif nums[j] == complement:
                    return [i, j]
"""

class Solution: #(better)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i
        return []
