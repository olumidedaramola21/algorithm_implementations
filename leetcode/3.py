# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest
# substring
#  without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        maxSubstring = 0
        charSet = set()

        while r < n:
            if s[r] not in charSet:
                charSet.add(s[r])
                maxSubstring = max(maxSubstring, r - l + 1)
                r += 1
            else:
                charSet.remove(s[l])
                l += 1
        return maxSubstring
