class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0 or not (n&(n-1)==0 and n%3==1):
            return False
        else:
            return True