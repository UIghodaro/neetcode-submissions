class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += str(len(string)) + '#'
            out += string

        return out 

    def decode(self, s: str) -> List[str]:
        print(s)
        out = []
        point = 0

        while point < len(s) - 1:
            num = ''

            # When you meet a # move 1 forward and then start eating
            while s[point] != '#':
                num += s[point]
                point += 1

            point += 1      # Skip the #
            string = ""     
            num = int(num)

            # Begin eating
            for i in range(num):
                string += s[point]
                point += 1

            out.append(string)

        return out

