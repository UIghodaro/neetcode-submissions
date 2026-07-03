# idea: 
# 1. Hash set, count elements in 1 pass
# 2. Some kind of data structures maintain what the top k are
# 3. Return what 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        out = heapq.nlargest(k, counter.keys(), key = counter.get)

        return out