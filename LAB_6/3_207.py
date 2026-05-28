from collections import deque, defaultdict

# Задача на поиск цикла в ориентированом графе


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)  # Список смежности
        in_degree = [
            0
        ] * numCourses  # Индекс — это номер курса, а значение — сколько у него невыполненных предварительных курсов

        for dest, src in prerequisites:  # [0,1]
            graph[src].append(dest)
            in_degree[dest] += 1

        queue = deque(
            [i for i in range(numCourses) if in_degree[i] == 0]
        )  # Прежметы для которых ничего не нужно сдавать, можно сразу идти на них

        visited_courses = 0

        while queue:
            course = queue.popleft()
            visited_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Сравниваю количество пройденных курсов с общим планом
        return visited_courses == numCourses
