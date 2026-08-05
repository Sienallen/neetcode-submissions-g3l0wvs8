class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        substring = set()
        res = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[left])
                left += 1 
            substring.add(s[r])
            res = max(res, len(substring))

        return res
        