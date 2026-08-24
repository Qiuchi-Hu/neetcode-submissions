class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        combs = []
        current = []
        num_of_digits = len(digits)

        def explore(index):
            if len(current) == num_of_digits:
                combs.append("".join(current))
                return
            
            for character in digit_map[digits[index]]:
                current.append(character)
                explore(index+1)
                current.pop()
        
        explore(0)
        #print(combs)
        return combs