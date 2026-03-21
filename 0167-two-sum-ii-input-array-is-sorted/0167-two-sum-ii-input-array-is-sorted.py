class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       #initializing two pointer , one from start the other in the end 
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]

            if s == target:
                return [left + 1, right + 1]
                #we add one because the array is one indexed 
            elif s < target:
                left += 1
            else:
                right -= 1
        