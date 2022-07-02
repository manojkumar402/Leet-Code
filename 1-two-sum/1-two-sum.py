class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Hashing method 2 sum problem
        d = {}
        for i in range(len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                return [d[target - nums[i]], i]