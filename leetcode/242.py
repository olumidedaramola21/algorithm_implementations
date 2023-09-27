from typing import List

# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = [0] * 26

        for char in s:
            char_count[ord(char) - ord("a")] += 1

        for char in t:
            char_count[ord(char) - ord("a")] -= 1
            if char_count[ord(char) - ord("a")] == 0:
                return False

        return True
