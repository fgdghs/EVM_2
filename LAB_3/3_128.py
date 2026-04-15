class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        max_len = 0

        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_len = 1

                while current_num + 1 in nums:
                    current_num += 1
                    current_len += 1

                max_len = max(max_len, current_len)

        return max_len


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
