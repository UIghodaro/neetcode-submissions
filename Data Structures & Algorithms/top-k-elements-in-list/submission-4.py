class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        return sorted(counts.keys(), reverse = True, key = counts.get)[:k]
        
        