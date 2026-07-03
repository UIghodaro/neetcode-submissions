class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        longest = set()
        count = 0

        for i in range(len(s)):
            if s[i] in longest:
                count = max(p2 - p1, count)
                while s[i] in longest:
                    longest.remove(s[p1])
                    p1 += 1
            longest.add(s[i])
            p2 += 1

        return max(p2 - p1, count)