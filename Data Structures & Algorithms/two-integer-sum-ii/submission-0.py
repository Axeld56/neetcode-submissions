class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # pour chaque élément dans la liste je regarde si on a 
        # target - element si oui on return les 2 sinon
        # on passe à l'élément suivant
        for number in numbers:
            if target - number in numbers:
                return [numbers.index(number)+1, numbers.index(target-number)+1]