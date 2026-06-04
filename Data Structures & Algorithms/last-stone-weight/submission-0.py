class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stone1 = max(stones)
            stones.remove(stone1)
            stone2 = max(stones)
            stones.remove(stone2)
            if stone1 == stone2:
                continue
            elif stone1 < stone2:
                stones.append(stone2-stone1)
            else:
                stones.append(stone1-stone2)
            
        if len(stones) == 1:
            return stones[0]
        return 0
        