class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
            print(f"i = {i}")
            print(f"nums[i] = {nums[i]}")
            print(f"nums[nums[i]] = {nums[nums[i]]}")
        return ans
