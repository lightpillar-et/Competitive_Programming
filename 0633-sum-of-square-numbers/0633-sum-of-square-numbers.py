class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        big = int (c**0.5)
        left ,right = 0, big 
        while left < right :
            s = left **2 + right **2 
            if s == c :
                return True 
            elif  s < c:
                left +=1
            else:
                right -=1
        return False 
            
        