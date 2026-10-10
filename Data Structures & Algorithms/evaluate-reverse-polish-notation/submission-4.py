class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                first = stack.pop()
                stack.append(stack.pop() - first)
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == '/':
                first = stack.pop()
                stack.append(int(stack.pop() / first))
            else:
                stack.append(int(tokens[i]))
        return stack[0]