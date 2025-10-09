class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = list(set(nums1))
        set2= list(set(nums2))
        distSet1, distSet2 = [], []
        for n in set1:
            if set2.count(n) == 0:
                distSet1.append(n)
        for n in set2:
            if set1.count(n) == 0:
                distSet2.append(n)
        return [distSet1, distSet2]
        


