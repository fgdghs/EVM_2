class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Использую две переменные для экономии памяти,
        # вместо создания целого массива dp
        prev2 = 0 # Максимум на два дома назад
        prev1 = 0 # Максимум на один дом назад

        for money in nums:
            # либо не грабим этот дом (prev1),
            # либо грабим (money + prev2)
            current = max(prev1, money + prev2)
            prev2 = prev1
            prev1 = current

        return prev1