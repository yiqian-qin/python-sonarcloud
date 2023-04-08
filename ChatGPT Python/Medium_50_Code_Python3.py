# Use the recursive binary exponentiation algorithm
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # base case
            if n == 0:
                return 1.0
            # recursive case
            half = helper(x, n // 2)
            if n % 2 == 0: # even case
                return half * half
            else: # odd case
                return half * half * x
        
        if n < 0:
            x = 1/x
            n = -n
        return helper(x, n)