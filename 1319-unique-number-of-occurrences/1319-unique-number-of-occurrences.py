class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for n in arr:
            if n in freq.keys():
                freq[n] += 1
            else:
                freq[n] = 1
        freqList = list(freq.values())
        return len(freqList) == len(set(freqList))