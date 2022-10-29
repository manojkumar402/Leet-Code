class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        self.vis = [0 for i in range(len(arr))]
        return self.solve(arr, start)
    def solve(self, arr, start):
        if start < 0 or start >= len(arr) or self.vis[start] == 1:
            return False

        if arr[start] == 0:
            return True
        self.vis[start] = 1
        a = self.solve(arr, start + arr[start])
        b = self.solve(arr, start - arr[start])
        return a or b