class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = []
        count = 0

        for i in range(len(s)):
            if s[i] in length:
                count = max(len(length), count)
                length = length[length.index(s[i]) + 1:]
            length.append(s[i])

        return max(len(length), count)