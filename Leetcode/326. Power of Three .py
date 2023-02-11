
class Solution:
    # def isPowerOfThree(n) -> bool:
    #     power = n**(1/3)
    #     if 3 == power:
    #         return print(True)
    #     else:
    #         return print(False)
    # isPowerOfThree(9)
     def isPowerOfThree(self, n: int) -> bool:
        #  return (n > 0) and 1162261467 % n == 0
        if n==1:
            return True
        if n%3!=0 or n<=0:
            return False
        else:
            n=n//3
            return self.isPowerOfThree(n)