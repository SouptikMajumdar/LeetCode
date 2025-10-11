class Solution:
    def removeStars(self, s: str) -> str:
        ans = ""
        starCount = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "*":
                starCount += 1
                continue
            else:
                if starCount != 0:
                    starCount -=1
                else:
                    ans = s[i] + ans
        return ans