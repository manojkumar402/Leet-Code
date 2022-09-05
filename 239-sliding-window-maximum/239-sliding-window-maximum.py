class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # fixed sliding window problem
        i = 0
        j = 0
        q = deque()
        res = []
        while j < len(nums):
            while len(q) > 0 and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])
            if j-i+1 == k:
                res.append(q[0])
                if nums[i] == q[0]:
                    q.popleft()
                i+=1
            j+=1
        return res
            
        