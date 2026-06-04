class Solution:
    def isHappy(self, n: int) -> bool:
        vu = set()

        while n != 1:
            if n in vu:
                return False
            vu.add(n)
            n = sum(int(d)**2 for d in str(n))

        return True
            
                
            