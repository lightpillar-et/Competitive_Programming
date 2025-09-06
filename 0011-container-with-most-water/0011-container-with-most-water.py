class Solution:
    def maxArea(self, nums: List[int]) -> int:
        area = 0 
        left , right = 0 ,len(nums) -1 
        while left < right :
            w = right - left 
            h = min (nums[right] ,  nums[left])
            cur_area = w * h 
            area = max (area , cur_area)

            if nums[left] < nums[right] :
                left +=1 
            elif nums[right] <= nums[left] :
                right -=1
        return area