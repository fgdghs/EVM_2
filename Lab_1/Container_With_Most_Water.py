class Solution:
    def maxArea(self, height: list[int]) -> int:
        Max_V = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            Max_V = max(
                Max_V,
                min(height[left_pointer], height[right_pointer])
                * (right_pointer - left_pointer),
            )

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return Max_V


print(Solution.maxArea(self=None, height=[1, 2, 1]))
