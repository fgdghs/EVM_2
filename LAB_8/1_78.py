class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            # Каждая остановка в функции — это готовое подмножество
            res.append(path)
            # start гарантирует, что мы не будем брать одни и те же элементы дважды и не будем идти назад
            for i in range(start, len(nums)):
                # path + [nums[i]]: Это создание нового списка
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res