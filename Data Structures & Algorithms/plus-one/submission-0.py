class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(str(d) for d in digits))
        n += 1
        return [d for d in str(n)]