class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, remaining):
            if not remaining:
                res.append(path)
                return
            # пробуем поставить на текущее место любое из оставшихся чисел
            for i in range(len(remaining)):
                # remaining[:i] + remaining[i+1:] берет всё, что стоит до элемента i и всё, что стоит после него, объединяя их
                # В итоге элемент i просто исключается из списка для следующего шага рекурсии
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return res