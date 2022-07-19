class Solution:
    def rob(self, nums: List[int]) -> int:
        # First and last elements cannot be taken 
        # so do a call for arr --> nums from 1 till len(nums)
        # 2nd call from ---> nums 0 till len(nums)-1
        if len(nums) == 1:
            return nums[0]
        dp1 = [-1 for i in range(len(nums))]
        dp2 = [-1 for i in range(len(nums))]
        ans1 = self.solve(nums, 1, dp1)
        nums.pop()
        ans2 = self.solve(nums, 0, dp2)
        return max(ans1, ans2)
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