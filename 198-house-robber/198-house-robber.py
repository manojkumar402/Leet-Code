class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]
        return self.solve(nums, 0, dp)
    def solve(self, nums, i, dp):
        if i >= len(nums):
            return 0
        
        if i == len(nums) - 1:
            return nums[i]
        if dp[i] != -1:
            return dp[i]
        # pick it 
        incl = self.solve(nums, i+2, dp) + nums[i]
        excl = self.solve(nums, i+1,dp)
        dp[i] = max(incl, excl)
        return dp[i]