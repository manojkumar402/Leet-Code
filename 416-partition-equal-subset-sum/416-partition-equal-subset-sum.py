class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # check the sum if sum is odd then we cannot split the array into two equal subsets
        if sum(nums) % 2 != 0:
            return False
        else:
            s = sum(nums) // 2
            dp = [[None for i in range(s+1)] for j in range(len(nums)+1)]
            # Intialization of the dp array
            for i in range(s+1):
                dp[0][i] = False
            for j in range(len(nums)+1):
                dp[j][0] = True
            # print(dp)
            for i in range(1, len(nums)+1):
                for j in range(1, s+1):
                    if nums[i-1] <= j:
                        # take it and leave it
                        dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
            return dp[len(nums)][s]
            
            
                    