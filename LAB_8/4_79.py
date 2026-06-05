class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # Если мы нашли все буквы (индекс равен длине слова)
            if i == len(word):
                return True

            # Проверка границ, совпадения буквы и того, что клетка не посещена
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[i]):
                return False

            # Помечаем клетку как посещенную
            temp = board[r][c]
            board[r][c] = '#'

            # Ищем следующую букву во всех 4 направлениях
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            #  возвращаем значение клетки обратно чтобы првоерить из всех точек графа
            board[r][c] = temp

            return found

        # Запуск поиска с каждой клетки
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False