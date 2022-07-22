class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        self.dp = [[-1 for i in range(2)] for j in range(len(nums1)+1)]
        # print(self.dp)
        return self.solve(nums1, nums2, 0, -1, -1, 0)
    def solve(self, a, b, i, prevA, prevB, swap):
        if i == len(a):
            return 0
        res = float('inf')
        if self.dp[i][swap] != -1:
            return self.dp[i][swap]
        if a[i] > prevA and b[i] > prevB:
            res = self.solve(a,b,i+1, a[i], b[i], 0) + 0
        if b[i] > prevA and a[i] > prevB:
            res = min(res, self.solve(a,b,i+1, b[i], a[i], 1) + 1)
        self.dp[i][swap] = res
        return res
       

