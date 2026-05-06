class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for item in strs:
            l = len(item)
            s += f'{l}>{item}'
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            length_of_item = ''
            while s[i] != '>':
                length_of_item += s[i]
                i += 1
            l = int(length_of_item)
            strs.append(s[i + 1: i + l + 1])
            i += l + 1

        return strs