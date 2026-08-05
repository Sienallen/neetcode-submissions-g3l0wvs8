class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        substring = ''
        res = 0

        while(right < len(s)):
            if(s[right] not in substring):
                substring += s[right]
                right += 1
            else: 
                substring = substring[1:]
                left += 1 
            res = max(res, len(substring))

        return res
        