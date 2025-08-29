class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        absolute = [abs (i)for i in nums]
        absolute.sort ()
        res = []
        for i in absolute :
            res.append (i**2)
        return res

        