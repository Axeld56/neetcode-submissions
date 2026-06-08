class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for w in strs:
            sw = ''.join(sorted(w))
            ana[sw].append(w)

        result = []
        for e in ana.values():
            result.append(e)
        return result