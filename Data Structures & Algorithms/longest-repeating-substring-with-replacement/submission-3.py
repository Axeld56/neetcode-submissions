class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, length = 0, 0
        for r, c in enumerate(s):
            count[c] += 1
            if not (r -l + 1) - max(count.values()) <= k:
                count[s[l]] -= 1
                l += 1
            length = max(length, r -l + 1)
        return length