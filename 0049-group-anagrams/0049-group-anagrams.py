class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for word in strs :
            cur = str (sorted(word))
            if cur in mapping :
                mapping[cur].append(word)
            else:
                mapping[cur] = [word]
        return list (mapping.values())
