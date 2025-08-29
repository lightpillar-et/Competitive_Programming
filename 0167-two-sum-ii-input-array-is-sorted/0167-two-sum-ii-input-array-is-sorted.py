class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right  = 0 , len(numbers) -1
        while left < right  :
            summ = numbers[left] + numbers[right]
            if summ  == target  :
                return ([left +1 , right +1])
            if summ < target :
                left +=1
            if summ > target :
                right -=1
        
        