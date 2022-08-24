class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = [[-1 for i in range(2*sum(nums) + 1)] for i in range(len(nums))]
        return self.findSumWays(nums, 0,0,target)
        
    

    def findSumWays(self, nums, i, tot, target)->int:
        
        if i == len(nums):
            if tot == target:
                return 1
            else:
                return 0
        else:
            if self.dp[i][tot+target] != -1:
                return self.dp[i][tot+target]
            a = self.findSumWays(nums, i+1, tot + nums[i], target)
            b = self.findSumWays(nums, i+1, tot - nums[i], target)
            self.dp[i][tot+target] = a + b
            return a + b
