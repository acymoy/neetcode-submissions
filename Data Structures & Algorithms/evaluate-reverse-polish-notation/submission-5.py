class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                value1 = stack.pop()
                value2 = stack.pop() 
                stack.append(value1 + value2)
            elif token == '-':
                value1 = stack.pop()
                value2 = stack.pop() 
                stack.append(value2 - value1)
            elif token == '*':
                value1 = stack.pop()
                value2 = stack.pop() 
                stack.append(value1 * value2)
            elif token == '/':
                value1 = stack.pop()
                value2 = stack.pop() 
                stack.append(math.trunc(value2 / value1))
            else:
                stack.append(int(token))
            print(stack)

        return stack.pop()