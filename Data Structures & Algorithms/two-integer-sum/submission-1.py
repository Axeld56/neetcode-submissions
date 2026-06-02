class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dico:
                return [dico[diff], i]
            dico[n] = i