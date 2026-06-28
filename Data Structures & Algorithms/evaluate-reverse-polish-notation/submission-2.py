class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+','-','*','/'])
        operands = []
        for t in tokens:
            result = 0
            if t in operators:
                op1 = operands.pop()
                op2 = operands.pop()
                result = 0
                if t == '+':
                    result = op1 + op2
                elif t == '-':
                    result = op2 - op1
                elif t == '*':
                    result = op1 * op2
                elif t == '/':
                    result = int(op2/op1)
            else:
                result = int(t)
            operands.append(result)
            print(operands)
        return operands[-1]