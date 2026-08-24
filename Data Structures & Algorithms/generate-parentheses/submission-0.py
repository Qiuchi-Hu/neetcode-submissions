class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        count = {
            "(":n,
            ")":n
        }

        list_of_parentheses = []
        current_parentheses = []
        total_count = 2*n

        def generate():
            if len(current_parentheses)==total_count:
                list_of_parentheses.append("".join(current_parentheses))
                return
            
            available_list = []
            if count["("]==count[")"]:
                available_list = ["("]
            elif count["("]<count[")"]:
                available_list = [")"]
                if count ["("]:
                    available_list.append("(")

            for current in available_list:
                current_parentheses.append(current)
                count[current] -=1
                generate()
                current_parentheses.pop()
                count[current] +=1
        
        generate()
        return list_of_parentheses