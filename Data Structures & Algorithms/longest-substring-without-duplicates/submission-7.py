class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        substr = s[0:1]
        max_len = 1
        l = 0
        r = 1
        while r+1 <= len(s):
            r += 1
            good = False
            while not good:
                if s[r-1] in s[l:r-1]:
                    l += 1
                else:
                    good = True
            max_len = max(max_len, len(s[l:r]))
        return max_len