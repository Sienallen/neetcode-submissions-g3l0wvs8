class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        substring = set()
        res = 0

        while(right < len(s)):
            if(s[right] not in substring):
                substring.add(s[right])
                right += 1
            else: 
                substring.remove(s[left])
                left += 1 
            res = max(res, len(substring))

        return res
        