class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        i = 0
        if len(s) == 0:
            return True
        while i < len(t):
            if s[s_i] == t[i]:
                s_i += 1
            if s_i == len(s):
                return True
            i += 1
        return False