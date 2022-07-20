class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[None for i in range(len(str1)+1)] for j in range(len(str2)+1)]
        for i in range(len(str1)+1):
            dp[0][i] = 0
        for j in range(len(str2)+1):
            dp[j][0] = 0

        for i in range(1, len(str2)+1):
            for j in range(1, len(str1)+1):
                if str1[j-1] == str2[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(len(str1)+len(str2)-dp[len(str2)][len(str1)])
        ans = "" 
        # for each in dp:
        #     print(each)
        i = len(str2)
        j = len(str1)
        while i > 0 and j > 0:
            if str1[j-1] == str2[i-1]:
                ans += str2[i-1]
                i-=1
                j-=1
            else:
                if dp[i][j-1] > dp[i-1][j]:
                    ans += str1[j-1]
                    j -= 1
                else:
                    ans += str2[i-1]
                    i -= 1
        while i > 0:
            ans += str2[i-1]
            i -= 1
        
        while j > 0:
            ans += str1[j-1]
            j -= 1
        return ans[::-1]
                    