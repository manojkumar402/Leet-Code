class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        ans = -1e6
        s = 0
        
        for i in range(k):
            s += nums[i]
        ans = max(ans, s/k)
        for i in range(k, len(nums)):
            s = s + nums[i] - nums[i-k]
            ans = max(ans, s/k)
        return ans
            