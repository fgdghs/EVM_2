import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2  # скорость поедания бананов

            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)

            if total_time <= h:
                # Успеет съесть, но можно попробовать медленее так как ищем минимальное
                res = k
                right = k - 1
            else:
                # Медленно
                left = k + 1

        return res


print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
