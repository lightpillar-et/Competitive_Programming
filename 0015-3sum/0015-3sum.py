class Solution:
    def threeSum(self, nums):
        #sorting the array so we can use two pointers easily
        nums.sort()
        result = []

        for i in range(len(nums)):
            #skipping duplicates , be defualt the first number is unique 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            cur = nums[i]
            left = i + 1
            right = len(nums) - 1
            #then do the two sum logic after we got out cur start 
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([cur, nums[left], nums[right]])

                    left += 1
                    right -= 1
                    #still skiping duplicates 
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result