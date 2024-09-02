class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return len(list(set(s)))
