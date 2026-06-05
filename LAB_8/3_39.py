class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(remaining, start, path):
            # Если остаток 0, значит мы нашли верную комбинацию
            if remaining == 0:
                res.append(path)
                return
            # Если остаток отрицательный, дальше идти нет смысла
            if remaining < 0:
                return

            # Перебор кандидатов, начиная с текущего индекса (start)
            # Это позволяет избежать дубликатов (например, [2,3] и [3,2])
            for i in range(start, len(candidates)):
                backtrack(remaining - candidates[i], i, path + [candidates[i]])

        backtrack(target, 0, [])
        return res