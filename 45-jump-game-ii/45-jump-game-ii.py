class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf') for i in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i, i+nums[i]+1):
                if j < len(nums):
                    dp[j] = min(dp[j], 1 + dp[i])
        # print(dp)
        return dp[-1]
        # return self.some(nums, 0)
        
    def some(self, nums, index) -> int:
        if index >= len(nums)-1:
            return 0
        mini = float('inf')
        if self.dp[index] != -1:
            return self.dp[index]
        for j in range(1, nums[index]+1):
            mini = min(mini, 1 + self.some(nums, index + j))
        self.dp[index] = mini
        return mini
                