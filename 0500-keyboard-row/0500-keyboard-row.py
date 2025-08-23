class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        r1 = "qwertyuiop "
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        for each in words:
            word = each.lower()
            if word[0] in r1:
                raw = r1
            elif word[0] in r2:
                raw = r2
            else:
                raw = r3

            for i in range(1, len(word)):
                if word[i] not in raw:
                    break
            else:
                res.append(each)
        return res
