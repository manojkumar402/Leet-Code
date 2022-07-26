class Solution:
    def findLongestChain(self, nums: List[List[int]]) -> int:
        N = len(nums)
        dp = [1] * N
        nums.sort()
        for i in range(N):
            for j in range(i):
                if nums[i][0] > nums[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)