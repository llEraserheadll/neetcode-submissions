class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in '+-/*':
                stack.append(int(token))
                continue
            
            number2 = stack.pop()
            number1 = stack.pop()
            result = 0

            if token == '+':
                result = number1+number2
            elif token == '-':
                result = number1 - number2
            elif  token == '*':
                result = number1 * number2
            else:
                result = int(number1 / number2)
            
            stack.append(result)

        return stack[0]