class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = float ("inf")
        profite = 0 
        
        for i in prices :
            if i < small :
                small = i 
            else:
                profite  = max (profite , i - small)
        return profite 
        