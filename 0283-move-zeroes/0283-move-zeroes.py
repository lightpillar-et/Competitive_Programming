class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left , right  = 0 , len(nums) -1
        while left < right :
            if nums[left] != 0 :
                left +=1
            else:
                nums.append (0)
                nums.pop(left)
                right -=1
          
                
        