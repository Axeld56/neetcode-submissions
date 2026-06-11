class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        length, l = 0, 0
        for r, c in enumerate(s):
            while c in sub:
                sub.remove(s[l])
                l += 1
            sub.add(c)
            length = max(length, r - l + 1)
        return length
                
                    
