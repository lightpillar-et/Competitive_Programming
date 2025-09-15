class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write , read = 0 , 0
        cnt  = 0 
        while read < len(nums) :
            if nums[read] != val :
                nums[write] = nums[read]
                write +=1 
                read +=1
                cnt +=1
            else :
                read +=1
        return cnt 
        