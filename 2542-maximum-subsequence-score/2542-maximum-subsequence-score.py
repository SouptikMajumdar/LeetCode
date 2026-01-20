class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = res = 0
        hp = []
        for a, b in sorted(list(zip(nums1, nums2)), key=lambda ab: -ab[1]):
            if len(hp) + 1 > k: 
                total -= heappop(hp) 
            heappush(hp, a)
            total = total + a 
            if len(hp) == k:
                res = max(res, b * total)
        return res