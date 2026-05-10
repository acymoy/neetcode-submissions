class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return len(s)
        
        res_set = set()
        res = 1
        l, r = 0, 0

        while r < len(s):
            print(res_set)
            if s[r] in res_set:
                while s[r] in res_set:
                    res_set.remove(s[l])
                    l += 1
            res_set.add(s[r])
            res = max(res, len(res_set))
            r += 1


        return res