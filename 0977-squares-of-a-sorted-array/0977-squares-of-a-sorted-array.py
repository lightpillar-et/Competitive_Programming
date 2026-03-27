class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res =[None] * len(nums)
        left , right = 0 , len(nums) -1
        tracker = len(nums) -1
        while left <= right :
            if nums[right] ** 2 > nums[left] **2 :
                res[tracker] = nums[right] ** 2
                right -=1
                tracker -=1
            else:
                res[tracker] = nums[left] **2
                tracker -=1
                left +=1
        return res



        