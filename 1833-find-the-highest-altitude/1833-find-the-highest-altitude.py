class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt, currAlt = 0, 0 
        for i in range(len(gain)):
            currAlt = currAlt + gain[i]
            maxAlt = max(maxAlt, currAlt)
        return maxAlt