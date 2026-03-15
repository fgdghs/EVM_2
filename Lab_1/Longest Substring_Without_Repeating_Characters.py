class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s.isspace():
            return 1
        if len(s) == 1:
            return 1
        Max_lenght = 0
        left_pointer = 0
        right_pointer = 0

        sub_string = set()

        while right_pointer < len(s):
            if s[right_pointer] not in sub_string:
                sub_string.add(s[right_pointer])
                right_pointer += 1
                Max_lenght = max(Max_lenght, len(sub_string))
            else:
                sub_string.remove(s[left_pointer])
                left_pointer += 1

        return Max_lenght


print(Solution.lengthOfLongestSubstring(self=None, s="abcabcbb"))
