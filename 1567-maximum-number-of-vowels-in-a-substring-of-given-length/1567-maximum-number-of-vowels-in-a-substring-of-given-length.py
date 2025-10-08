class Solution:
    def countVowels(self, s: str) -> int:
        vowels = ["a","e","i","o","u"]
        count = 0
        if s == "":
            return 0
        for char in s:
            if char in vowels:
                count += 1
        return count
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a","e","i","o","u"]
        max_v = 0
        for i in range(0, len(s)-k+1):
            if i == 0:
                num_v = self.countVowels(s[i:i+k])
            else:
                if s[i-1] in vowels:
                    num_v -= 1
                if s[i+k-1] in vowels:
                    num_v += 1
            if num_v > max_v:
                max_v = num_v
        return max_v
