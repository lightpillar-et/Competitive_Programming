class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #converting to list so we can work with chunks 
        chars = list(s)
        # we step by 2*k becuase we are working in subsection
        for start in range(0, len(chars), 2 * k):

            left = start
            #our reverse portion is the first k letters and based on the constraints if it go out  or if it less than we adjust it like this 
            right = min(start + k - 1, len(chars) - 1)
            #reverse 
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)