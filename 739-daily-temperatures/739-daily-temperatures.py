class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        s = []
        for i in range(len(temperatures)-1, -1,-1):
            if len(s) == 0:
                ans.append(0)
            elif len(s) > 0 and s[-1][0] > temperatures[i]:
                ans.append(s[-1][1] - i)
            elif len(s) > 0 and s[-1][0] <= temperatures[i]:
                while len(s) > 0 and s[-1][0] <= temperatures[i]:
                    s.pop()
                if len(s) == 0:
                    ans.append(0)
                else:
                    ans.append(s[-1][1] - i)
            s.append((temperatures[i], i))
        ans = ans [::-1]
        return ans
        #TLE j loop dependent of i loop use stack
        # for i in range(len(temperatures)):
        #     count = 1
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             ans[i] = count
        #             break
        #         else:
        #             count+=1
        # return ans
        
        