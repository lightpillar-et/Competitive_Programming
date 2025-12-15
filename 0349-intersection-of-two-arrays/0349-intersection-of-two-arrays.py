class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res =[]
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        i , j = 0 , 0

        while i < n1  and j < n2 :
            if nums1[i] == nums2[j] :
                res.append(nums1[i])
                i+=1
                j+=1
                while i < n1 and i >0 :
                    if nums1[i] == nums1[i-1]:
                        i +=1 
                    else:
                        break 
                while j < n2 and j >0 :
                    if nums2[j] == nums2[j-1]:
                        j+=1
                    else:
                        break 
               
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1
        return res


        