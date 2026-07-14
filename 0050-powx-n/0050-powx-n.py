class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        result = 1.0
        cp = x
        while power > 0:
                if power % 2 == 1:
                    result *= cp
                cp *= cp
                power //= 2
        return result if n >= 0 else 1.0 / result
