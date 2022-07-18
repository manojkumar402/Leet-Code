class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.dp = [-1 for i in range(target)]
        return self.memo(nums, target)
    def memo(self, nums, target):
        c = 0
        if target == 0:
            return 1
        if target < 0:
            return 0
        if self.dp[target-1] != -1:
            return self.dp[target-1]
        for num in nums:
            c += self.memo(nums, target-num)
        self.dp[target-1] = c
        return self.dp[target-1]