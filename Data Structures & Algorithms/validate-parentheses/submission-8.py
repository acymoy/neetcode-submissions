class Solution:
    def isValid(self, s: str) -> bool:
        m = {'[': ']', '{': '}', '(': ')'}

        if len(s) % 2:
            return False
        
        stack = []
        for l in s:
            if l in m.keys():
                stack.append(m[l])
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if popped != l:
                    return False
        return len(stack) == 0