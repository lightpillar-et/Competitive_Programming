class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0
        while i < len (s) :
            rotated  =  s [i :] + s[:i]
            if rotated == goal:
                return True 
            i+=1
        
        return False 
        