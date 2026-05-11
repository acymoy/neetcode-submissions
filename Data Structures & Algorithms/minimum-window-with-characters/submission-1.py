class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        s_map = {}
        t_map = {}
        min_y = -1
        min_x = -1
        res_length = float('inf')

        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        need = len(t_map.values())
        have = 0

        l = 0
        for r in range(len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            if s[r] in t_map and t_map[s[r]] == s_map[s[r]]:
                have += 1

            while have == need:
                print('we have what we need at ', s[l: r + 1])
                print(have, need)
                if res_length > (r - l + 1):
                    res_length = r - l + 1
                    min_y = l
                    min_x = r + 1

                s_map[s[l]] -= 1
                if s[l] in t_map and t_map[s[l]] > s_map[s[l]]:
                    have -= 1
                l += 1

        if min_y + min_x < 0:
            return ''
        return s[min_y: min_x]