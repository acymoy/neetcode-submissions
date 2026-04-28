class Solution:
    def countLetters(self, s: str):
        m = {}
        for l in s:
            if l not in m.keys():
                m[l] = 1
            else:
                m[l] += 1
        return m

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = self.countLetters(s)
        t_map = self.countLetters(t)

        return s_map == t_map
        