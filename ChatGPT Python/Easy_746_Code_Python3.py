# Using dp to solve the problem
# dp[i] means the minimum cost to reach the ith step on the floor
# dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        # set dp[0] and dp[1] to the first and second item of cost because we can start from either step 0 or step 1
        dp[0], dp[1] = cost[0], cost[1] 
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # the final result should be the minimum of last two steps
        return min(dp[n-1], dp[n-2])