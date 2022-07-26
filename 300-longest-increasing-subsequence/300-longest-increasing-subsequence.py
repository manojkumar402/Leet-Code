class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i] = 1 + dp[j]
        print(dp)
        return max(dp)