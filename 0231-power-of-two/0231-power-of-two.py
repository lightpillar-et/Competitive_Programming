class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def power (n) :
            if n ==1 :
                return True 
            if n < 2  and n != 1:
                return False 
            elif n == 2:
                return True 
            else:
                return (power (n / 2))
        res = power (n)
        return res
        
             
        