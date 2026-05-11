class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        # key formula is window - mostFreq >= k
        res = 0
        window_map = {}
        l = 0

        for r in range(len(s)):
            window_map[s[r]] = 1 + window_map.get(s[r], 0)
            if (r - l + 1) - max(window_map.values()) <= k:
                res = max(res, r - l + 1)
            while (r - l + 1) - max(window_map.values()) > k:
                window_map[s[l]] -= 1
                l += 1


        return res