class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profite = 0 
        i   , j = 0 ,1 
        while j < len(prices) :
            if prices [i] < prices[j] :
                profite = max (profite , prices[j] - prices[i])
                j+=1
            else:
                i =j
                j+=1
        return profite 


        