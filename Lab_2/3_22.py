class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = [(0, 0, "")]
        while stack:
            open_skobka, closed_skobka, s = stack.pop()
            if len(s) == n * 2:
                res.append(s)
                continue
            if open_skobka < n:
                stack.append((open_skobka + 1, closed_skobka, s + "("))
            if closed_skobka < open_skobka:
                stack.append((open_skobka, closed_skobka + 1, s + ")"))
            print(stack)
        return res


print(Solution.generateParenthesis(self=None, n=3))
