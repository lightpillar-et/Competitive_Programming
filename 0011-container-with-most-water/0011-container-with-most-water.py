class Solution:
    def maxArea(self, height: List[int]) -> int:
        left ,right  = 0 , len(height)-1 
        area = 0
        while left < right :
            width = right - left 
            length = min(height[left] , height[right])
            cur_area =  width * length
            if cur_area > area :
                area = cur_area
            if height[right] > height[left]:
                left +=1
            else:
                right -=1
        return area     