class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        odd1, odd2 = 0, 0 
        freq1, freq2 = {}, {}
        
        for c1 in set(word1):
            count1 = word1.count(c1)
            freq1[c1] = word1.count(c1)
        
        set2 = set(word2)
        for c2 in set2:
            if c2 not in freq1:
                return False
            freq2[c2] = word2.count(c2)

        freq1 = list(freq1.values())
        freq2 = list(freq2.values())

        freq1.sort()
        freq2.sort()

        for i in range(len(freq1)):
            if freq1[i] != freq2[i]:
                return False
            
        return True
            
        
            

         