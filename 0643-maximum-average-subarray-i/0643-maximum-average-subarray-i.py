class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float ("-inf")
        window_sum = 0
        left = 0 
        for right in range (len(nums)) :
            window_sum  += nums [right]
            if right  - left +1 == k :
                 print (right , left , left +1 )
                 res = max (window_sum / k , res)
                 window_sum  = window_sum - nums[left]
                 left +=1 
        return res
              
        