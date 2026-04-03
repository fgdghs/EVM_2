class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        res = []
        for i in tokens:
            if i == "+":
                res.append(res.pop() + res.pop())
            elif i == "-":
                a = res.pop()
                b = res.pop()
                res.append(b - a)
            elif i == "*":
                res.append(res.pop() * res.pop())
            elif i == "/":
                a = res.pop()
                b = res.pop()
                res.append(int(b / a))
            else:
                res.append(int(i))
        return res[0]


print(Solution.evalRPN(self=None, tokens=["2", "1", "+", "3", "*"]))
