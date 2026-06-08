class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
    
        kp = 0
        result = []
        while kp != k:
            best = max(count, key = count.get)
            result.append(best)
            del count[best]
            kp += 1
        return result