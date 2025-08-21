class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = [""]
        for i in digits:
            letter = phone [i]
            new_list = []
            for j in res :
                for z in letter :
                    new_list.append (j+z)
            res = new_list
        return res
        