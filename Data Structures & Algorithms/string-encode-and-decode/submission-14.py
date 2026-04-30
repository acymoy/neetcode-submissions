class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            to_append = f"{len(word)}|{word}"
            s += to_append
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '|':
                j += 1
                print(s[j])
            length = int(s[i:j])
            print('word length is ', length)
            result.append(s[j + 1: j + length + 1])
            i = j + length + 1
        return result
