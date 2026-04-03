class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dick = {"{": "}", "(": ")", "[": "]"}

        for i in s:
            if i in dick.keys():
                stack.append(i)
            else:
                if not stack:
                    return False

                last_open = stack.pop()
                if dick[last_open] != i:
                    return False

        return len(stack) == 0


sol = Solution()
print(sol.isValid(")"))
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))
