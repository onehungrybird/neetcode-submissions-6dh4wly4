class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        for i in range(0, len(strs)):
            l_i = []
            for j in strs:
                if sorted(j) == sorted(strs[i]):
                    l_i.append(j)
            if l_i not in l:
                l.append(l_i)
        return l
        