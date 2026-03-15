
# arr = [1,2,2,4]


# setarr = set(arr)
# if len(arr) == len(setarr):
#     print("True")
# else:
#     print("False")

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit,profit)
            else:
                left = right
            right += 1

        return max_profit

    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        
        for i in range(k,len(nums)):

            cur_sum = cur_sum + nums[i]
            cur_sum = cur_sum - nums[i - k]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum / k
    

