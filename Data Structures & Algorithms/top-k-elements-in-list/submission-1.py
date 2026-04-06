from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        l = []
        sorted_d = sorted(d.items(), key = lambda item : item[1])
        for i in sorted_d[-k:]:
            l.append(i[0])
        return l