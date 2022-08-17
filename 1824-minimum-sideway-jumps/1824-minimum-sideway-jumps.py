class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        
        self.dp = [[-1 for i in range(4)]for j in range(len(obstacles)+1)]
        def solve(i, obs, lane):
            ans = float('inf')
            if i == len(obs)-1:
                return 0
            if self.dp[i][lane] != -1:
                return self.dp[i][lane]
            if obs[i+1] == 0:
                return solve(i+1, obs, lane)
            elif obs[i+1] != lane:
                return solve(i+1, obs,lane)
            else:
                # jump in all the sides
                for k in range(1, 4):
                    if obs[i] != k and k != lane:
                        ans = min(ans, solve(i+1, obs, k) + 1)
            self.dp[i][lane] = ans
            return ans
        return solve(0, obstacles, 2)
            
        # lane, obstacles, count, i 
#         self.c = float('inf')
#         def solve(i, obs, count, lane):
#             if i == len(obs)-1:
#                 self.c = min(self.c, count)
#                 return 
#             if obs[i+1] == 0:
#                 solve(i+1, obs, count, lane)
#             elif obs[i+1] != lane:
#                 solve(i+1, obs, count, lane)
#             else:
#                 # jump in all the sides
#                 for k in range(1, 4):
#                     if obs[i] != k and k != lane:
#                         solve(i+1, obs, count+1, k)
#         solve(-1, obstacles, 0, 2)
#         return self.c
        
                        
                        
                    
        
        
    