class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prod = math.prod(nums[:i]) * math.prod(nums[i+1:])
            result.append(prod)
        return result