class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum (nums[:k]) 
        left , right = 0 , k
        while right <len(nums) :
            cur_window = window_sum - nums[left] + nums[right]
            window_sum = max (window_sum , cur_window)
            left +=1
            right +=1
        return window_sum / k
            


        