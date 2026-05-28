class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit_set, prev_height):
            if (
                r < 0  # Вышли за границы матрицы
                or c < 0  # Вышли за границы матрицы
                or r >= rows  # Вышли за границы матрицы
                or c >= cols  # Вышли за границы матрицы
                or (r, c) in visit_set  # Ячейка уже посещена этим океаном
                or heights[r][c]
                < prev_height  # Высота новой ячейки МЕНЬШЕ предыдущей (вода не может течь вверх от океана)
            ):
                return

            # Помечаем ячейку как достижимую для текущего океана
            visit_set.add((r, c))

            dfs(r + 1, c, visit_set, heights[r][c])  # вниз
            dfs(r - 1, c, visit_set, heights[r][c])  # вверх
            dfs(r, c + 1, visit_set, heights[r][c])  # вправо
            dfs(r, c - 1, visit_set, heights[r][c])  # влево

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])  # Верхняя строка  Тихий
            dfs(
                rows - 1, c, atlantic, heights[rows - 1][c]
            )  # Нижня строка  Атлантический
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])  # Левый столбец Тихий
            dfs(
                r, cols - 1, atlantic, heights[r][cols - 1]
            )  # Правый столбец Атлантический

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
