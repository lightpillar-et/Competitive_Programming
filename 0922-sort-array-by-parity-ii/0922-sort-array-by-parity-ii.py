class Solution:
    def sortArrayByParityII(self, nums):
        even = []
        odd = []
        res = []

        for x in nums:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

        e = o = 0  

        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even[e])
                e += 1
            else:
                res.append(odd[o])
                o += 1

        return res
