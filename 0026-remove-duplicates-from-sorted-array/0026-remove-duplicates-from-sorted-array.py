class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums :
            return 0
        write = 0 
        for i in range (1, len(nums)):
            if nums[write] != nums[i]:
                write += 1
                nums[write] = nums[i]
        return write +1

        