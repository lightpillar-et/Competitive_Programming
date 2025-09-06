class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0 
        write  = 0 
        while read < len(nums) :
            if nums[read] == 0 :
                read+=1
                continue 
            else:
                nums[write] , nums[read] = nums[read] , nums[write]
                write +=1
                read+=1
        