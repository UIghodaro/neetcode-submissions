# This solution is now authentically mine, technically I had knowledge of the answer prior but did not remember if this was the correct approach, I just did what made sense
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        l = top = 0

        for r in range(len(s)):
            # The count letter we are tracking must necessarily be greater than or equal to (<size of the window> - k) as there are at most k replacements
            count[s[r]] += 1
            top = max(top, count[s[r]])

            while top < r - l - k + 1:
                count[s[l]] -= 1
                l += 1
                top = max(top, count[s[l]])

        return r - l + 1