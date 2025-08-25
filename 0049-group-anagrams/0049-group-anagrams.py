class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for each in strs :
            key = "".join (sorted (each))
            if key not in res :
                res [key] = [each]

            else :
                res [key].append (each)
        return list (res.values ())




        