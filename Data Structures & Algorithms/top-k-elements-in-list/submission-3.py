# idea: 
# 1. Hash map, count elements in 1 pass
# 2. Some kind of data structures maintain what the top k are
# 3. Return what 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        sortedKeys = []

        for item in nums:
            count[item] += 1

        # Heap operations, even shorter
        return heapq.nlargest(k, count.keys(), key = count.get)