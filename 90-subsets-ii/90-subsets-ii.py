from copy import copy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.help(0, nums, len(nums), [], res)
        return res
        
    def help(self, i, nums, n, subset, powerset):
        if i == n:
            powerset.append(copy(subset))
            return 
        
        subset.append(nums[i])
        self.help(i+1, nums, n, subset, powerset)
        subset.pop()
        # make changes for duplicate values in testcase
        
        while i < n - 1 and nums[i] == nums[i+1]:
            i+=1
        self.help(i+1, nums, n, subset, powerset)
            