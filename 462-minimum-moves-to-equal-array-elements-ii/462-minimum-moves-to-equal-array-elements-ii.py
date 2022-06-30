class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        if len(nums) % 2 == 0:
            mid = len(nums) // 2 - 1
        else:
            mid = len(nums) // 2
        for i in range(len(nums)):
            ans = ans + abs(nums[i] - nums[mid])
        return ans
        

        