class Solution:
    def isPalindrome(self, s: str) -> bool:
        stroka = "".join(char.lower() for char in s if char.isalnum())
        return stroka == stroka[::-1]


print(Solution.isPalindrome(self=None, s="A man, a plan, a canal: Panama"))
