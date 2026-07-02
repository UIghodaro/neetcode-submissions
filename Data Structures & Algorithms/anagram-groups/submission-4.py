class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = dict()
        out = []
        count = 0


        for word in strs:
            sort = "".join(sorted(word))
            if sort in key:
                out[key[sort]].append(word)
            else:
                out.append([word])
                key[sort] = count
                count += 1

        return out