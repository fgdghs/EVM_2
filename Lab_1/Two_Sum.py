class Solution:
    def __init__(self, name):
        self.name = name

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dick = {} 
            
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dick:
                return [dick[diff], i]
            dick[n] = i
        return
        



a = Solution("Test")

print(a.twoSum([2,7,11,15],9))
print(a.twoSum([3,2,4],6))
print(a.twoSum([3,3],6))