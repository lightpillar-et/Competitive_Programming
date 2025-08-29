class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [None] * len (nums)
        left , right = 0 , len(nums) -1 
        location  = len(nums) -1 

        while left <=right  :
            left_square = nums[left] ** 2
            right_square = nums [right] **2
          

            if right_square >= left_square :
                res[location] = right_square
                right -=1
            else:
                res[location] = left_square
                left +=1
            location -=1

        return res

        