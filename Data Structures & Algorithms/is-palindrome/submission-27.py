class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not ((s[l] >= 'a' and s[l] <= 'z') or (s[l] >= '0' and s[l] <= '9')):
                l += 1
            while l < r and not  ((s[r] >= 'a' and s[r] <= 'z') or (s[r] >= '0' and s[r] <= '9')):
                r -= 1
            print(s[l], ' ', s[r])
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True