class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        left = 0
        s = 0
        for i in range(n):
            s += nums[i]
            while s >= target:
                ans = min(ans, i + 1 - left)
                s -= nums[left]
                left += 1
        if ans == float('inf'):
            return 0
        return ans