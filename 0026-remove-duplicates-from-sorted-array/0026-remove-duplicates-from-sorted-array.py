class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        left, right = 0, 0

        while right < len(nums):
            if nums[right] not in seen:
                seen.add(nums[right])        
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

          
