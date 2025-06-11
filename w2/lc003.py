class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest = 0
        left = 0
        substring = set()
        for i in range(0, len(s)):
            while s[i] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[i])
            if len(substring) > longest:
                longest = len(substring)

        return longest
