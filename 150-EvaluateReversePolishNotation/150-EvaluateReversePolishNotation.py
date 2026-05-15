# Last updated: 15/05/2026, 11:45:18
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token.lstrip('-').isdigit():
                stack.append(int(token))

            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    result = num2 + num1

                elif token == '-':
                    result = num2 - num1

                elif token == '*':
                    result = num2 * num1

                elif token == '/':
                    result = int(num2 / num1)

                stack.append(result)

        return stack[-1]