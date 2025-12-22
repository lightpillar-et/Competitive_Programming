class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [None] * n 
        idx = n -1

        left , right = 0 , len(nums)-1
        while left <= right :
            if nums[right] ** 2  > nums[left] **2 :
                res[idx] = nums[right] ** 2
                idx -=1
                right -=1
            else:
                res[idx] = nums[left] **2 
                left +=1
                idx -=1
        return res

        