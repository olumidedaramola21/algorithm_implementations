# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Solution 1
# Solution uses extra memory
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ""
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]


# Solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            )

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while r > l and not alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True
