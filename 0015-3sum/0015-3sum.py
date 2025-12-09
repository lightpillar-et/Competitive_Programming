class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                 
        res = []                  

        for i in range(len(nums)):  
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = -nums[i]     # inverse logic

            while left < right:
                two_sum = nums[left] + nums[right]

                if two_sum < target:
                    left += 1
                elif two_sum > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates on left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates on right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res
