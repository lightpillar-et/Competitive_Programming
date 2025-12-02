class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = sorted(nums , key = lambda x: abs(x))
        res =[]
        for i in nums:
            res.append(i**2)
        return res
        