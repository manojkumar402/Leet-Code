class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]
        return self.solve(nums, len(nums)-1, dp)
    def solve(self, nums, n, dp):
        if n < 0:
            return 0
        
        if n == 0:
            return nums[n]
        if dp[n] != -1:
            return dp[n]
        # pick it 
        incl = self.solve(nums, n-2, dp) + nums[n]
        excl = self.solve(nums, n-1,dp)
        dp[n] = max(incl, excl)
        return dp[n]