class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        # dp[i] хранит длину самой длинной подпоследовательности, заканчивающейся на i-ом элементе
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # Если текущий элемент nums[i] больше предыдущего nums[j],
                    # мы можем продлить цепочку, заканчивающуюся на j, добавив к ней текущий элемент.
                    # Выбираем максимум между текущим значением dp[i] и новой длиной (dp[j] + 1).
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)