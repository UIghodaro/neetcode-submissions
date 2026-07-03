# idea: 
# 1. Hash set, count elements in 1 pass
# 2. Some kind of data structures maintain what the top k are
# 3. Return what 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = defaultdict(int)
        sortedKeys = []

        for num in nums:
            numCounter[num] += 1

        frequencies = sorted(numCounter, key = numCounter.get, reverse = True)
        for i in range(k):
            sortedKeys.append(frequencies[i])

        return sortedKeys