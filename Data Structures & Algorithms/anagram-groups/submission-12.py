class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lookup = defaultdict(list)
        
        for word in strs:
            lookup[str(sorted(word))].append(word)

        return [lookup[key] for key in lookup]