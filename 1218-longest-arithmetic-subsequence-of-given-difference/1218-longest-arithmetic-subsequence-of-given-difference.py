class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans=0
        dp={}
        for x in arr:
            if x-difference in dp:
                dp[x]=dp[x-difference]+1
            else:
                dp[x]=1
            ans=max(ans, dp[x])
        return ans