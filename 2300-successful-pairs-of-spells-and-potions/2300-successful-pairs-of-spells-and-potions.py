class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        for spell in spells:
            check = ceil(success / spell)
            #res = [spell * p for p in potions]
            if potions[-1] < check:
                pairs.append(0)
                continue
            if potions[0] >= check:
                pairs.append(len(potions))
                continue
            # Binary Search
            index = len(potions) // 2
            s_i, s_j = 0, len(potions) - 1
            while s_i < s_j:
                if index < len(potions)-1 and potions[index] < check and potions[index+1] >= check:
                    pairs.append(len(potions) - index - 1)
                    break
                elif index == len(potions)-1 and potions[index] >= check:
                    pairs.append(1)
                    break
                elif potions[index] >= check:
                    s_j = index
                elif potions[index] < check:
                    s_i = index + 1
                index = (s_i + s_j) // 2
                if s_i == s_j:
                    pairs.append(0) 
        return pairs

                

