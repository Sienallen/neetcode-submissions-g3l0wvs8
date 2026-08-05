class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        substring = defaultdict(int )
        res = 0

        while(right < len(s)):
            if(s[right] not in substring or substring[s[right]] < 1):
                substring[s[right]] += 1
                right += 1
            else: 
                substring[s[left]] -= 1 
                left += 1 
            res = max(res, sum(substring.values()))

        return res
        