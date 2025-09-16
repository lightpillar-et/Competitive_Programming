class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum (nums[:k])
        res = window_sum / k
        for i in range (k , len(nums)):
            window_sum += nums[i] - nums[i - k]
            
            res = max (window_sum / k, res)
        return res 

        