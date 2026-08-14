class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set (nums)
        longest  = 0
      

        for i in nums :
            cur = 1
            if i -1 not in nums :
               

                while i +1 in nums :
                    cur +=1
                    i+=1
            longest = max (cur , longest)
        return longest 


        