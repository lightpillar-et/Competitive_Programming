class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort ()
        opp =0
        left = 0 
        right  = len (nums) -1

        while left < right  :
            s =nums [left] + nums [right]
            if s == k :
                opp +=1
                left +=1
                right -=1
            elif s < k  :
                left +=1
            else :
                right -=1
        return opp
        