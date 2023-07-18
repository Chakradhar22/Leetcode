class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a=len(text1)
        b=len(text2)
        dp=[[0]*(a+1) for _ in range(b+1)]
        for i in range(1,b+1):
            for j in range(1,a+1):
                if text1[j-1]==text2[i-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[b][a]