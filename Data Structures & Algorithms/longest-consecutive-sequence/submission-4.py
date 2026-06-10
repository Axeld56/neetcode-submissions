class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length, tmp = 0, 1
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                tmp = 1
            else:
                while num + 1 in nums:
                    tmp += 1
                    num += 1
                if tmp > length:
                    length = tmp
        
        return length