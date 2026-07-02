class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = defaultdict(list)

        for word in strs:
            sort = "".join(sorted(word))
            key[sort].append(word)

        return list(key.values())