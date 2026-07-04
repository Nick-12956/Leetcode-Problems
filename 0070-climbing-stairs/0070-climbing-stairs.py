class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        # the number of ways to reach the previous step
        prev = 3
        # the number of ways to reach the previous-previous step
        prev_prev = 2
        current = 0

        for _ in range(3, n):
            current = prev + prev_prev
            prev_prev = prev
            prev = current
        
        return current