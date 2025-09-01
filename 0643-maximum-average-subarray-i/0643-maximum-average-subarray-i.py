class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum (nums[:k])
        max_window =  window_sum  
        left = 0 
        for right in range (k , len(nums)):
            window_sum  += nums[right] - nums[left]
            left +=1 
            max_window = max (window_sum , max_window)
        return max_window / k
        