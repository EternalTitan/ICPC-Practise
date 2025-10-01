class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        p = 0
        record = {}
        for i in range(len(s)):
            if s[i] in record and record[s[i]] >= p:
                p = record[s[i]] + 1
            else:
                if i - p + 1 > result:
                    result = i - p + 1
            record[s[i]] = i
        return result


print(Solution().lengthOfLongestSubstring("tmmzuxt"))
