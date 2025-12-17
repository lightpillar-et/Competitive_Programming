class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        #BruteForce
        container1 = []
        container2 = []
        for i in nums :
            if  i % 2 == 0:
                container1.append(i)
            else:
                container2.append(i)
        return container1 + container2